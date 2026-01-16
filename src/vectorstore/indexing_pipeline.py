# src/vectorstore/indexing_pipeline.py

import sys
import os
from typing import List, Dict, Optional
from pathlib import Path
import json
import logging
from tqdm import tqdm

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

if __name__ == "__main__":
    # Add project root to path for direct execution
    project_root = Path(__file__).resolve().parent.parent.parent
    sys.path.insert(0, str(project_root))

from src.preprocessing.pipeline import PreprocessingPipeline
from src.splitter.cisco_splitter import CiscoManualSplitter
from src.embedding.embedding_service import CiscoEmbeddingService
from src.vectorstore.chroma_store import CiscoVectorStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IndexingPipeline:
    """
    PDF → 벡터 DB 전체 인덱싱 파이프라인
    """
    
    def __init__(
        self,
        output_dir: str = "./processed",
        vectordb_dir: str = "./vectordb",
        embedding_model: str = "BAAI/bge-m3",
        chunk_size: int = 800,
        chunk_overlap: int = 100
    ):
        """
        Args:
            output_dir: 전처리 결과 저장 경로
            vectordb_dir: 벡터 DB 저장 경로
            embedding_model: 임베딩 모델
            chunk_size: 청크 크기
            chunk_overlap: 청크 오버랩
        """
        self.output_dir = Path(output_dir)
        self.vectordb_dir = Path(vectordb_dir)
        
        # 컴포넌트 초기화
        self.preprocessor = PreprocessingPipeline(str(self.output_dir))
        self.splitter = CiscoManualSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        self.embedding_service = CiscoEmbeddingService(model_name=embedding_model)
        self.vector_store = CiscoVectorStore(
            persist_directory=str(self.vectordb_dir),
            embedding_service=self.embedding_service
        )
    
    def index_pdf(
        self,
        pdf_path: str,
        device_type: str = "unknown",
        nxos_version: str = "unknown"
    ) -> Dict:
        """
        단일 PDF 인덱싱
        
        Args:
            pdf_path: PDF 파일 경로
            device_type: 장비 타입 (예: "Nexus 9000")
            nxos_version: IOS 버전 (예: "17.x")
            
        Returns:
            인덱싱 결과 정보
        """
        result = {
            'source': pdf_path,
            'status': 'success',
            'chunks_indexed': 0,
            'errors': []
        }
        
        try:
            # 1. 전처리 (PDF → Markdown → 챕터 분할)
            logger.info(f"Step 1: Preprocessing {pdf_path}")
            preprocess_result = self.preprocessor.process(
                pdf_path,
                split_level=2
            )
            
            all_chunks = []
            
            # 2. 각 챕터를 청크로 분할
            logger.info("Step 2: Chunking chapters")
            for chapter_info in tqdm(preprocess_result['chapters'], desc="Chunking"):
                chapter_path = chapter_info['filepath']
                
                with open(chapter_path, 'r', encoding='utf-8') as f:
                    chapter_content = f.read()
                
                # 기본 메타데이터
                base_metadata = {
                    'source': pdf_path,
                    'device_type': device_type,
                    'nxos_version': nxos_version,
                    'chapter': chapter_info['title'],
                    'page_range': chapter_info['page_range']
                }
                
                # 청크 분할
                chunks = self.splitter.split_document(
                    chapter_content,
                    metadata=base_metadata
                )
                
                all_chunks.extend(chunks)
            
            logger.info(f"Total chunks created: {len(all_chunks)}")
            
            # 3. 벡터 DB에 인덱싱
            logger.info("Step 3: Indexing to vector store")
            doc_ids = self.vector_store.add_documents(all_chunks)
            
            result['chunks_indexed'] = len(doc_ids)
            result['chapters_processed'] = len(preprocess_result['chapters'])
            
        except Exception as e:
            logger.error(f"Indexing failed: {e}")
            result['status'] = 'failed'
            result['errors'].append(str(e))
        
        return result
    
    def index_directory(
        self,
        pdf_directory: str,
        device_mapping: Optional[Dict[str, Dict]] = None
    ) -> Dict:
        """
        디렉토리 내 모든 PDF 인덱싱
        
        Args:
            pdf_directory: PDF 파일들이 있는 디렉토리
            device_mapping: 파일명별 장비 정보 매핑
            
        Returns:
            전체 인덱싱 결과
        """
        pdf_dir = Path(pdf_directory)
        pdf_files = list(pdf_dir.glob("*.pdf"))
        
        logger.info(f"Found {len(pdf_files)} PDF files")
        
        results = {
            'total_files': len(pdf_files),
            'successful': 0,
            'failed': 0,
            'details': []
        }
        
        device_mapping = device_mapping or {}
        
        for pdf_file in pdf_files:
            # 장비 정보 조회
            file_info = device_mapping.get(
                pdf_file.name,
                {'device_type': 'unknown', 'nxos_version': 'unknown'}
            )
            
            logger.info(f"\nProcessing: {pdf_file.name}")
            
            result = self.index_pdf(
                str(pdf_file),
                device_type=file_info.get('device_type', 'unknown'),
                nxos_version=file_info.get('nxos_version', 'unknown')
            )
            
            results['details'].append(result)
            
            if result['status'] == 'success':
                results['successful'] += 1
            else:
                results['failed'] += 1
        
        # 최종 통계 저장
        stats_path = self.output_dir / "indexing_stats.json"
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        logger.info(f"\nIndexing complete: {results['successful']}/{results['total_files']} successful")
        
        return results


# 실행 예시
if __name__ == "__main__":
    # 파이프라인 초기화
    pipeline = IndexingPipeline(
        output_dir="./processed",
        vectordb_dir="./vectordb",
        embedding_model="BAAI/bge-m3",
        chunk_size=800
    )
    
    # 단일 파일 인덱싱
    result = pipeline.index_pdf(
        pdf_path="./manuals/Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guid_10.5(x)_150_200.pdf",
        device_type="Nexus 9000",
        nxos_version="10.5(x)"
    )
    
    print(f"인덱싱 완료: {result['chunks_indexed']}개 청크")
    
    # 벡터 스토어 통계 확인
    stats = pipeline.vector_store.get_collection_stats()
    print(f"전체 문서 수: {stats['total_documents']}")