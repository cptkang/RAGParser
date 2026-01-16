# src/parser/layout_parser.py

import os
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import fitz  # PyMuPDF
import pdfplumber
from unstructured.partition.pdf import partition_pdf
from unstructured.documents.elements import (
    Title, NarrativeText, ListItem, Table, Image, Header, Footer
)


class ElementType(Enum):
    """문서 요소 타입 정의"""
    TITLE = "title"
    HEADER = "header"
    PARAGRAPH = "paragraph"
    LIST_ITEM = "list_item"
    TABLE = "table"
    CODE_BLOCK = "code_block"
    WARNING = "warning"
    NOTE = "note"
    IMAGE = "image"


@dataclass
class DocumentElement:
    """파싱된 문서 요소"""
    type: ElementType
    content: str
    page_number: int
    bbox: Optional[Tuple[float, float, float, float]] = None
    metadata: Dict = field(default_factory=dict)
    level: int = 0  # 헤더 레벨 (1-6)


@dataclass
class Chapter:
    """챕터 단위 문서"""
    title: str
    level: int
    content: str
    page_start: int
    page_end: int
    elements: List[DocumentElement] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)


class CiscoManualParser:
    """
    시스코 매뉴얼 Layout-Aware 파서
    
    특징:
    - 테이블 구조 보존
    - CLI 명령어 블록 인식
    - 경고/주의 박스 처리
    - 한글 인코딩 지원
    """
    
    # 시스코 CLI 프롬프트 패턴
    CLI_PATTERNS = [
        r'^(Router|Switch|Device|hostname)[>#]',
        r'^[\w\-]+[>#]',
        r'^[\w\-]+\(config[^\)]*\)#',
    ]
    
    # 경고/주의 키워드
    WARNING_KEYWORDS = ['경고', '주의', 'Warning', 'Caution', 'Note', '참고']
    
    def __init__(self, use_gpu: bool = False):
        self.use_gpu = use_gpu
        self.cli_pattern = re.compile('|'.join(self.CLI_PATTERNS), re.MULTILINE)
        
    def parse_pdf(self, pdf_path: str) -> List[DocumentElement]:
        """
        PDF를 Layout-Aware 방식으로 파싱
        
        Args:
            pdf_path: PDF 파일 경로
            
        Returns:
            DocumentElement 리스트
        """
        elements = []
        
        # unstructured를 사용한 Layout 분석
        raw_elements = partition_pdf(
            filename=pdf_path,
            strategy="hi_res",  # 고해상도 레이아웃 분석
            infer_table_structure=True,  # 테이블 구조 추론
            languages=["kor", "eng"],  # 한국어 + 영어
            include_page_breaks=True,
        )
        
        current_page = 1
        
        for elem in raw_elements:
            # 페이지 번호 추적
            if hasattr(elem, 'metadata') and elem.metadata.page_number:
                current_page = elem.metadata.page_number
            
            doc_elem = self._convert_element(elem, current_page)
            if doc_elem:
                elements.append(doc_elem)
        
        # 후처리: CLI 블록 병합
        elements = self._merge_cli_blocks(elements)
        
        return elements
    
    def _convert_element(
        self, 
        elem, 
        page_number: int
    ) -> Optional[DocumentElement]:
        """unstructured 요소를 DocumentElement로 변환"""
        
        text = str(elem).strip()
        if not text:
            return None
            
        # 요소 타입 판별
        elem_type = ElementType.PARAGRAPH
        level = 0
        metadata = {}
        
        if isinstance(elem, Title):
            elem_type = ElementType.TITLE
            level = self._detect_header_level(text)
        elif isinstance(elem, Header):
            elem_type = ElementType.HEADER
            level = self._detect_header_level(text)
        elif isinstance(elem, ListItem):
            elem_type = ElementType.LIST_ITEM
        elif isinstance(elem, Table):
            elem_type = ElementType.TABLE
            text = self._table_to_markdown(elem)
        elif self._is_cli_block(text):
            elem_type = ElementType.CODE_BLOCK
            metadata['code_type'] = 'cisco_cli'
        elif self._is_warning_block(text):
            elem_type = ElementType.WARNING
            metadata['warning_type'] = self._get_warning_type(text)
            
        return DocumentElement(
            type=elem_type,
            content=text,
            page_number=page_number,
            level=level,
            metadata=metadata
        )
    
    def _detect_header_level(self, text: str) -> int:
        """헤더 레벨 감지"""
        # 시스코 매뉴얼의 일반적인 패턴
        patterns = [
            (r'^Chapter\s+\d+', 1),
            (r'^제\s*\d+\s*장', 1),
            (r'^\d+\.\s+[A-Z가-힣]', 2),
            (r'^\d+\.\d+\s+', 3),
            (r'^\d+\.\d+\.\d+\s+', 4),
        ]
        
        for pattern, level in patterns:
            if re.match(pattern, text):
                return level
        return 2  # 기본값
    
    def _is_cli_block(self, text: str) -> bool:
        """CLI 명령어 블록 여부 확인"""
        return bool(self.cli_pattern.search(text))
    
    def _is_warning_block(self, text: str) -> bool:
        """경고/주의 블록 여부 확인"""
        return any(kw in text[:50] for kw in self.WARNING_KEYWORDS)
    
    def _get_warning_type(self, text: str) -> str:
        """경고 타입 추출"""
        for kw in self.WARNING_KEYWORDS:
            if kw in text[:50]:
                return kw.lower()
        return "note"
    
    def _table_to_markdown(self, table_elem) -> str:
        """테이블을 Markdown 형식으로 변환"""
        if hasattr(table_elem, 'metadata') and table_elem.metadata.text_as_html:
            # HTML 테이블을 Markdown으로 변환
            return self._html_table_to_markdown(table_elem.metadata.text_as_html)
        return str(table_elem)
    
    def _html_table_to_markdown(self, html: str) -> str:
        """HTML 테이블을 Markdown 테이블로 변환"""
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        if not table:
            return html
            
        rows = table.find_all('tr')
        if not rows:
            return html
            
        md_lines = []
        
        for i, row in enumerate(rows):
            cells = row.find_all(['td', 'th'])
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            md_lines.append('| ' + ' | '.join(cell_texts) + ' |')
            
            # 헤더 구분선
            if i == 0:
                md_lines.append('|' + '|'.join(['---'] * len(cells)) + '|')
        
        return '\n'.join(md_lines)
    
    def _merge_cli_blocks(
        self, 
        elements: List[DocumentElement]
    ) -> List[DocumentElement]:
        """연속된 CLI 블록 병합"""
        merged = []
        cli_buffer = []
        
        for elem in elements:
            if elem.type == ElementType.CODE_BLOCK:
                cli_buffer.append(elem)
            else:
                if cli_buffer:
                    merged.append(self._create_merged_cli(cli_buffer))
                    cli_buffer = []
                merged.append(elem)
        
        if cli_buffer:
            merged.append(self._create_merged_cli(cli_buffer))
            
        return merged
    
    def _create_merged_cli(
        self, 
        cli_elements: List[DocumentElement]
    ) -> DocumentElement:
        """CLI 요소들을 하나로 병합"""
        content = '\n'.join(elem.content for elem in cli_elements)
        return DocumentElement(
            type=ElementType.CODE_BLOCK,
            content=content,
            page_number=cli_elements[0].page_number,
            metadata={'code_type': 'cisco_cli', 'line_count': len(cli_elements)}
        )