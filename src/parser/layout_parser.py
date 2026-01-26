# src/parser/layout_parser.py

import os
import re
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import fitz  # PyMuPDF
import pdfplumber

# 로거 설정
logger = logging.getLogger(__name__)

# unstructured 조건부 import (NLTK 의존성)
UNSTRUCTURED_AVAILABLE = False
try:
    from unstructured.partition.pdf import partition_pdf
    from unstructured.documents.elements import (
        Title, NarrativeText, ListItem, Table, Image, Header, Footer
    )
    UNSTRUCTURED_AVAILABLE = True
except ImportError:
    logger.warning("unstructured 라이브러리를 찾을 수 없습니다. PyMuPDF 모드로 동작합니다.")


def check_nltk_data() -> bool:
    """NLTK 데이터 사용 가능 여부 확인"""
    try:
        import nltk
        nltk.data.find('tokenizers/punkt_tab')
        nltk.data.find('taggers/averaged_perceptron_tagger_eng')
        return True
    except (ImportError, LookupError):
        return False


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
    - 오프라인 모드 지원 (PyMuPDF fallback)
    """

    # 시스코 CLI 프롬프트 패턴
    CLI_PATTERNS = [
        r'^(Router|Switch|Device|hostname)[>#]',
        r'^[\w\-]+[>#]',
        r'^[\w\-]+\(config[^\)]*\)#',
    ]

    # 경고/주의 키워드
    WARNING_KEYWORDS = ['경고', '주의', 'Warning', 'Caution', 'Note', '참고']

    def __init__(self, use_gpu: bool = False, force_offline: bool = False):
        """
        Args:
            use_gpu: GPU 사용 여부
            force_offline: True면 항상 PyMuPDF 모드 사용
        """
        self.use_gpu = use_gpu
        self.force_offline = force_offline
        self.cli_pattern = re.compile('|'.join(self.CLI_PATTERNS), re.MULTILINE)

        # unstructured 사용 가능 여부 확인
        self._use_unstructured = (
            UNSTRUCTURED_AVAILABLE
            and check_nltk_data()
            and not force_offline
        )

        if self._use_unstructured:
            logger.info("Parser 모드: unstructured (NLTK)")
        else:
            logger.info("Parser 모드: PyMuPDF (오프라인)")

    def parse_pdf(self, pdf_path: str) -> List[DocumentElement]:
        """
        PDF를 Layout-Aware 방식으로 파싱

        Args:
            pdf_path: PDF 파일 경로

        Returns:
            DocumentElement 리스트
        """
        if self._use_unstructured:
            try:
                return self._parse_pdf_unstructured(pdf_path)
            except Exception as e:
                logger.warning(f"unstructured 파싱 실패, PyMuPDF로 전환: {e}")
                return self._parse_pdf_pymupdf(pdf_path)
        else:
            return self._parse_pdf_pymupdf(pdf_path)

    def _parse_pdf_unstructured(self, pdf_path: str) -> List[DocumentElement]:
        """unstructured를 사용한 PDF 파싱 (기본 모드)"""
        elements = []

        raw_elements = partition_pdf(
            filename=pdf_path,
            strategy="hi_res",
            infer_table_structure=True,
            languages=["kor", "eng"],
            include_page_breaks=True,
        )

        current_page = 1

        for elem in raw_elements:
            if hasattr(elem, 'metadata') and elem.metadata.page_number:
                current_page = elem.metadata.page_number

            doc_elem = self._convert_element_unstructured(elem, current_page)
            if doc_elem:
                elements.append(doc_elem)

        elements = self._merge_cli_blocks(elements)
        return elements

    def _parse_pdf_pymupdf(self, pdf_path: str) -> List[DocumentElement]:
        """PyMuPDF를 사용한 PDF 파싱 (오프라인 모드)"""
        elements = []
        doc = fitz.open(pdf_path)

        # pdfplumber로 테이블 영역 추출
        table_regions = self._extract_table_regions(pdf_path)

        for page_num, page in enumerate(doc, 1):
            page_tables = table_regions.get(page_num, [])

            # 텍스트 블록 추출 (dict 모드로 상세 정보 포함)
            blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

            for block in blocks:
                if block["type"] == 0:  # 텍스트 블록
                    bbox = block["bbox"]

                    # 테이블 영역 내의 텍스트는 건너뛰기 (별도 처리)
                    if self._is_in_table_region(bbox, page_tables):
                        continue

                    # 텍스트 추출
                    text = self._extract_block_text(block)
                    if not text.strip():
                        continue

                    # 요소 타입 판별
                    doc_elem = self._classify_element(text, page_num, bbox, block)
                    if doc_elem:
                        elements.append(doc_elem)

            # 테이블 추가
            for table_data in page_tables:
                table_elem = DocumentElement(
                    type=ElementType.TABLE,
                    content=table_data['markdown'],
                    page_number=page_num,
                    bbox=table_data['bbox'],
                    metadata={'rows': table_data.get('rows', 0)}
                )
                elements.append(table_elem)

        doc.close()

        # 후처리
        elements = self._merge_cli_blocks(elements)
        elements = self._sort_elements_by_position(elements)

        return elements

    def _extract_table_regions(self, pdf_path: str) -> Dict[int, List[Dict]]:
        """pdfplumber를 사용하여 테이블 영역 추출"""
        table_regions = {}

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    tables = page.find_tables()
                    page_tables = []

                    for table in tables:
                        # 테이블 데이터 추출
                        table_data = table.extract()
                        if table_data:
                            markdown = self._table_data_to_markdown(table_data)
                            page_tables.append({
                                'bbox': table.bbox,
                                'markdown': markdown,
                                'rows': len(table_data)
                            })

                    if page_tables:
                        table_regions[page_num] = page_tables
        except Exception as e:
            logger.warning(f"테이블 추출 실패: {e}")

        return table_regions

    def _table_data_to_markdown(self, table_data: List[List]) -> str:
        """테이블 데이터를 Markdown으로 변환"""
        if not table_data:
            return ""

        md_lines = []

        for i, row in enumerate(table_data):
            # None 값 처리
            cells = [str(cell) if cell else "" for cell in row]
            md_lines.append('| ' + ' | '.join(cells) + ' |')

            # 첫 번째 행 후 구분선
            if i == 0:
                md_lines.append('|' + '|'.join(['---'] * len(cells)) + '|')

        return '\n'.join(md_lines)

    def _is_in_table_region(
        self,
        bbox: Tuple[float, float, float, float],
        tables: List[Dict]
    ) -> bool:
        """좌표가 테이블 영역 내에 있는지 확인"""
        x0, y0, x1, y1 = bbox

        for table in tables:
            tx0, ty0, tx1, ty1 = table['bbox']
            # 겹치는 영역 확인
            if x0 < tx1 and x1 > tx0 and y0 < ty1 and y1 > ty0:
                return True
        return False

    def _extract_block_text(self, block: Dict) -> str:
        """블록에서 텍스트 추출"""
        text_parts = []

        for line in block.get("lines", []):
            line_text = ""
            for span in line.get("spans", []):
                line_text += span.get("text", "")
            text_parts.append(line_text)

        return '\n'.join(text_parts)

    def _classify_element(
        self,
        text: str,
        page_number: int,
        bbox: Tuple[float, float, float, float],
        block: Dict
    ) -> Optional[DocumentElement]:
        """텍스트를 분류하여 DocumentElement 생성"""
        text = text.strip()
        if not text:
            return None

        elem_type = ElementType.PARAGRAPH
        level = 0
        metadata = {}

        # 폰트 정보로 헤더 감지
        font_size = self._get_dominant_font_size(block)
        is_bold = self._is_bold_text(block)

        # 헤더 감지 (큰 폰트 또는 볼드)
        if font_size and font_size > 12 or is_bold:
            if self._is_header_pattern(text):
                elem_type = ElementType.TITLE
                level = self._detect_header_level(text)

        # CLI 블록 감지
        if self._is_cli_block(text):
            elem_type = ElementType.CODE_BLOCK
            metadata['code_type'] = 'cisco_cli'
        # 경고 블록 감지
        elif self._is_warning_block(text):
            elem_type = ElementType.WARNING
            metadata['warning_type'] = self._get_warning_type(text)
        # 리스트 아이템 감지
        elif self._is_list_item(text):
            elem_type = ElementType.LIST_ITEM

        return DocumentElement(
            type=elem_type,
            content=text,
            page_number=page_number,
            bbox=bbox,
            level=level,
            metadata=metadata
        )

    def _get_dominant_font_size(self, block: Dict) -> Optional[float]:
        """블록의 주요 폰트 크기 반환"""
        sizes = []
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if "size" in span:
                    sizes.append(span["size"])
        return max(sizes) if sizes else None

    def _is_bold_text(self, block: Dict) -> bool:
        """볼드 텍스트 여부 확인"""
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                flags = span.get("flags", 0)
                # flags & 2^4 = bold
                if flags & 16:
                    return True
                # 폰트 이름에 Bold 포함
                font = span.get("font", "")
                if "Bold" in font or "bold" in font:
                    return True
        return False

    def _is_header_pattern(self, text: str) -> bool:
        """헤더 패턴 확인"""
        patterns = [
            r'^Chapter\s+\d+',
            r'^제\s*\d+\s*장',
            r'^\d+\.\s+[A-Z가-힣]',
            r'^\d+\.\d+',
        ]
        return any(re.match(p, text) for p in patterns)

    def _is_list_item(self, text: str) -> bool:
        """리스트 아이템 여부 확인"""
        patterns = [
            r'^[\•\-\*]\s+',
            r'^\d+\)\s+',
            r'^[a-z]\)\s+',
            r'^Step\s+\d+',
        ]
        return any(re.match(p, text) for p in patterns)

    def _sort_elements_by_position(
        self,
        elements: List[DocumentElement]
    ) -> List[DocumentElement]:
        """요소를 페이지 및 위치 순으로 정렬"""
        def sort_key(elem):
            page = elem.page_number
            y = elem.bbox[1] if elem.bbox else 0
            x = elem.bbox[0] if elem.bbox else 0
            return (page, y, x)

        return sorted(elements, key=sort_key)

    def _convert_element_unstructured(
        self,
        elem,
        page_number: int
    ) -> Optional[DocumentElement]:
        """unstructured 요소를 DocumentElement로 변환"""

        text = str(elem).strip()
        if not text:
            return None

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
        return 2

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
