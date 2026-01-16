# src/preprocessing/pipeline.py

import os
from pathlib import Path
from typing import List, Dict, Optional
import json
import logging

# Setup poppler path for PDF processing
def setup_poppler():
    """Add poppler to PATH if available"""
    project_root = Path(__file__).resolve().parent.parent.parent
    poppler_bin = project_root / ".venv" / "poppler" / "poppler-24.08.0" / "Library" / "bin"

    if poppler_bin.exists():
        os.environ["PATH"] = str(poppler_bin) + os.pathsep + os.environ.get("PATH", "")
        return True
    return False

setup_poppler()

from ..parser.layout_parser import CiscoManualParser, DocumentElement
from ..parser.markdown_converter import MarkdownConverter, ChapterSplitter, Chapter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PreprocessingPipeline:
    """
    PDF → Markdown → 챕터 분할 파이프라인
    """
    
    def __init__(self, output_dir: str = "./processed"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.parser = CiscoManualParser()
        self.converter = MarkdownConverter()
        self.splitter = ChapterSplitter()
        
    def process(
        self, 
        pdf_path: str,
        split_level: int = 2,  # 섹션 레벨에서 분할
        save_intermediate: bool = True
    ) -> Dict:
        """
        전체 전처리 파이프라인 실행
        
        Args:
            pdf_path: 입력 PDF 경로
            split_level: 챕터 분할 기준 레벨
            save_intermediate: 중간 결과물 저장 여부
            
        Returns:
            처리 결과 정보
        """
        pdf_name = Path(pdf_path).stem
        doc_output_dir = self.output_dir / pdf_name
        doc_output_dir.mkdir(exist_ok=True)
        
        result = {
            'source': pdf_path,
            'output_dir': str(doc_output_dir),
            'chapters': [],
            'statistics': {}
        }
        
        # 1. Layout-Aware Parsing
        logger.info(f"Parsing PDF: {pdf_path}")
        elements = self.parser.parse_pdf(pdf_path)
        logger.info(f"Extracted {len(elements)} elements")
        
        result['statistics']['total_elements'] = len(elements)
        
        # 중간 결과 저장
        if save_intermediate:
            self._save_elements(elements, doc_output_dir / "elements.json")
        
        # 2. 전체 Markdown 변환
        logger.info("Converting to Markdown")
        full_markdown = self.converter.convert(elements)
        
        if save_intermediate:
            with open(doc_output_dir / "full_document.md", 'w', encoding='utf-8') as f:
                f.write(full_markdown)
        
        # 3. 챕터 분할
        logger.info(f"Splitting into chapters (level={split_level})")
        chapters = self.splitter.split_by_chapters(elements, split_level)
        logger.info(f"Created {len(chapters)} chapters")
        
        result['statistics']['total_chapters'] = len(chapters)
        
        # 4. 챕터별 파일 저장
        chapter_dir = doc_output_dir / "chapters"
        chapter_files = self.splitter.split_to_files(chapters, str(chapter_dir))
        
        # 결과 정보 수집
        for chapter, filepath in zip(chapters, chapter_files):
            result['chapters'].append({
                'title': chapter.title,
                'filepath': filepath,
                'page_range': f"{chapter.page_start}-{chapter.page_end}",
                'element_count': len(chapter.elements),
                'char_count': len(chapter.content)
            })
        
        # 메타데이터 저장
        with open(doc_output_dir / "metadata.json", 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Processing complete. Output: {doc_output_dir}")
        return result
    
    def _save_elements(
        self, 
        elements: List[DocumentElement], 
        filepath: Path
    ):
        """요소 정보를 JSON으로 저장"""
        data = []
        for elem in elements:
            data.append({
                'type': elem.type.value,
                'content': elem.content[:500],  # 미리보기용 제한
                'page': elem.page_number,
                'level': elem.level,
                'metadata': elem.metadata
            })
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


# 실행 예시
if __name__ == "__main__":
    pipeline = PreprocessingPipeline(output_dir="./processed_manuals")
    
    # 시스코 매뉴얼 처리
    result = pipeline.process(
        pdf_path="./manuals/cisco_catalyst_9000_config.pdf",
        split_level=2  # 섹션 레벨에서 분할
    )
    
    print(f"처리 완료: {result['statistics']['total_chapters']}개 챕터 생성")