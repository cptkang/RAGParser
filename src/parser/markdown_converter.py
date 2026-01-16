# src/parser/markdown_converter.py

from typing import List, Dict
from .layout_parser import DocumentElement, ElementType, Chapter
import re


class MarkdownConverter:
    """
    DocumentElement를 Markdown으로 변환
    
    시스코 매뉴얼 특화:
    - CLI 명령어 코드 블록 처리
    - 경고/주의 Admonition 처리
    - 테이블 포맷 유지
    """
    
    def __init__(self):
        self.toc = []  # 목차
        
    def convert(self, elements: List[DocumentElement]) -> str:
        """전체 문서를 Markdown으로 변환"""
        md_parts = []
        
        for elem in elements:
            md_part = self._convert_element(elem)
            if md_part:
                md_parts.append(md_part)
        
        return '\n\n'.join(md_parts)
    
    def _convert_element(self, elem: DocumentElement) -> str:
        """단일 요소를 Markdown으로 변환"""
        
        converters = {
            ElementType.TITLE: self._convert_header,
            ElementType.HEADER: self._convert_header,
            ElementType.PARAGRAPH: self._convert_paragraph,
            ElementType.LIST_ITEM: self._convert_list_item,
            ElementType.TABLE: self._convert_table,
            ElementType.CODE_BLOCK: self._convert_code_block,
            ElementType.WARNING: self._convert_warning,
            ElementType.NOTE: self._convert_warning,
        }
        
        converter = converters.get(elem.type, self._convert_paragraph)
        return converter(elem)
    
    def _convert_header(self, elem: DocumentElement) -> str:
        """헤더 변환"""
        level = min(elem.level, 6) if elem.level > 0 else 2
        header = '#' * level + ' ' + elem.content
        
        # 목차에 추가
        self.toc.append({
            'level': level,
            'title': elem.content,
            'page': elem.page_number
        })
        
        return header
    
    def _convert_paragraph(self, elem: DocumentElement) -> str:
        """일반 텍스트 변환"""
        return elem.content
    
    def _convert_list_item(self, elem: DocumentElement) -> str:
        """리스트 아이템 변환"""
        # 번호 있는 리스트인지 확인
        if re.match(r'^\d+\.', elem.content):
            return elem.content
        return f"- {elem.content}"
    
    def _convert_table(self, elem: DocumentElement) -> str:
        """테이블 변환 (이미 Markdown 형식이면 그대로)"""
        return elem.content
    
    def _convert_code_block(self, elem: DocumentElement) -> str:
        """코드 블록 변환"""
        code_type = elem.metadata.get('code_type', '')
        
        # 시스코 CLI는 특별 표시
        if code_type == 'cisco_cli':
            return f"```cisco-ios\n{elem.content}\n```"
        return f"```\n{elem.content}\n```"
    
    def _convert_warning(self, elem: DocumentElement) -> str:
        """경고/주의 블록 변환 (Admonition 형식)"""
        warning_type = elem.metadata.get('warning_type', 'note')
        
        # Markdown Admonition 형식
        type_map = {
            '경고': 'warning',
            '주의': 'caution', 
            'warning': 'warning',
            'caution': 'caution',
            'note': 'note',
            '참고': 'info'
        }
        
        admon_type = type_map.get(warning_type, 'note')
        
        return f"> **{admon_type.upper()}**\n> {elem.content}"
    
    def get_toc(self) -> str:
        """목차 생성"""
        toc_lines = ["# 목차\n"]
        
        for item in self.toc:
            indent = "  " * (item['level'] - 1)
            toc_lines.append(f"{indent}- [{item['title']}](#{self._slugify(item['title'])})")
        
        return '\n'.join(toc_lines)
    
    def _slugify(self, text: str) -> str:
        """헤더 ID용 슬러그 생성"""
        slug = text.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[\s_]+', '-', slug)
        return slug


class ChapterSplitter:
    """
    Markdown 문서를 챕터별로 분할
    """
    
    def __init__(self, min_chapter_length: int = 500):
        self.min_chapter_length = min_chapter_length
    
    def split_by_chapters(
        self, 
        elements: List[DocumentElement],
        split_level: int = 1  # 분할 기준 헤더 레벨
    ) -> List[Chapter]:
        """
        문서를 챕터 단위로 분할
        
        Args:
            elements: 파싱된 문서 요소들
            split_level: 분할 기준이 될 헤더 레벨 (1=최상위)
            
        Returns:
            Chapter 리스트
        """
        chapters = []
        current_chapter = None
        converter = MarkdownConverter()
        
        for elem in elements:
            # 새 챕터 시작 감지
            is_chapter_start = (
                elem.type in [ElementType.TITLE, ElementType.HEADER] 
                and elem.level <= split_level
            )
            
            if is_chapter_start:
                # 이전 챕터 저장
                if current_chapter and current_chapter.elements:
                    current_chapter.content = converter.convert(current_chapter.elements)
                    current_chapter.page_end = current_chapter.elements[-1].page_number
                    chapters.append(current_chapter)
                
                # 새 챕터 시작
                current_chapter = Chapter(
                    title=elem.content,
                    level=elem.level,
                    content="",
                    page_start=elem.page_number,
                    page_end=elem.page_number,
                    elements=[elem],
                    metadata={'header_level': elem.level}
                )
            elif current_chapter:
                current_chapter.elements.append(elem)
            else:
                # 첫 챕터 이전 내용 (서문 등)
                current_chapter = Chapter(
                    title="Introduction",
                    level=0,
                    content="",
                    page_start=elem.page_number,
                    page_end=elem.page_number,
                    elements=[elem],
                    metadata={'is_preface': True}
                )
        
        # 마지막 챕터 저장
        if current_chapter and current_chapter.elements:
            current_chapter.content = converter.convert(current_chapter.elements)
            current_chapter.page_end = current_chapter.elements[-1].page_number
            chapters.append(current_chapter)
        
        return chapters
    
    def split_to_files(
        self, 
        chapters: List[Chapter], 
        output_dir: str
    ) -> List[str]:
        """챕터를 개별 Markdown 파일로 저장"""
        import os
        
        os.makedirs(output_dir, exist_ok=True)
        file_paths = []
        
        for i, chapter in enumerate(chapters):
            # 파일명 생성 (안전한 문자만)
            safe_title = re.sub(r'[^\w\s-]', '', chapter.title)[:50]
            filename = f"{i+1:02d}_{safe_title}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 메타데이터 헤더 추가
            content = self._add_frontmatter(chapter)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            file_paths.append(filepath)
        
        return file_paths
    
    def _add_frontmatter(self, chapter: Chapter) -> str:
        """YAML frontmatter 추가"""
        frontmatter = f"""---
title: "{chapter.title}"
page_start: {chapter.page_start}
page_end: {chapter.page_end}
level: {chapter.level}
---

"""
        return frontmatter + chapter.content