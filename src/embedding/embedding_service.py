# src/embedding/embedding_service.py

from typing import List, Dict, Optional, Union
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document
import torch
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CiscoEmbeddingService:
    """
    시스코 매뉴얼을 위한 임베딩 서비스
    
    특징:
    - 배치 처리로 효율적 임베딩
    - CLI 명령어와 설명 텍스트 구분 처리
    - 쿼리/문서 프리픽스 지원 (E5 모델용)
    """
    
    # E5 모델용 프리픽스
    QUERY_PREFIX = "query: "
    PASSAGE_PREFIX = "passage: "
    
    def __init__(
        self,
        model_name: str = "BAAI/bge-m3",
        device: Optional[str] = None,
        use_prefix: bool = True,
        batch_size: int = 32
    ):
        """
        Args:
            model_name: 임베딩 모델 이름/경로
            device: cuda/cpu (None이면 자동 선택)
            use_prefix: E5 스타일 프리픽스 사용 여부
            batch_size: 배치 크기
        """
        self.model_name = model_name
        self.use_prefix = use_prefix and 'e5' in model_name.lower()
        self.batch_size = batch_size
        
        # 디바이스 설정
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        logger.info(f"Loading embedding model: {model_name}")
        logger.info(f"Device: {self.device}")
        
        # 모델 로드
        self.model = SentenceTransformer(
            model_name,
            device=self.device
        )
        
        self.dimension = self.model.get_sentence_embedding_dimension()
        logger.info(f"Embedding dimension: {self.dimension}")
    
    def embed_documents(
        self,
        documents: List[Document],
        show_progress: bool = True
    ) -> List[Dict]:
        """
        문서 리스트 임베딩
        
        Args:
            documents: Document 리스트
            show_progress: 진행 상황 표시
            
        Returns:
            임베딩 결과 (벡터 + 메타데이터)
        """
        results = []
        texts = []
        
        for doc in documents:
            text = doc.page_content
            
            # CLI 명령어 블록 특수 처리
            if doc.metadata.get('chunk_type') == 'cli_command':
                text = self._preprocess_cli(text)
            
            # E5 프리픽스 추가
            if self.use_prefix:
                text = self.PASSAGE_PREFIX + text
                
            texts.append(text)
        
        # 배치 임베딩
        embeddings = self._batch_encode(texts, show_progress)
        
        for doc, embedding in zip(documents, embeddings):
            results.append({
                'embedding': embedding,
                'content': doc.page_content,
                'metadata': doc.metadata
            })
        
        return results
    
    def embed_query(self, query: str) -> np.ndarray:
        """
        쿼리 임베딩 (검색용)
        
        Args:
            query: 검색 쿼리
            
        Returns:
            쿼리 임베딩 벡터
        """
        if self.use_prefix:
            query = self.QUERY_PREFIX + query
            
        embedding = self.model.encode(
            query,
            normalize_embeddings=True,
            convert_to_numpy=True
        )
        
        return embedding
    
    def embed_queries(self, queries: List[str]) -> np.ndarray:
        """
        다중 쿼리 임베딩
        """
        if self.use_prefix:
            queries = [self.QUERY_PREFIX + q for q in queries]
            
        embeddings = self.model.encode(
            queries,
            normalize_embeddings=True,
            convert_to_numpy=True,
            batch_size=self.batch_size
        )
        
        return embeddings
    
    def _batch_encode(
        self, 
        texts: List[str],
        show_progress: bool = True
    ) -> np.ndarray:
        """배치 인코딩"""
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            batch_size=self.batch_size,
            show_progress_bar=show_progress
        )
        
        return embeddings
    
    def _preprocess_cli(self, text: str) -> str:
        """
        CLI 명령어 전처리
        
        - 프롬프트 정규화
        - 주요 명령어 강조
        """
        # 프롬프트 정규화
        import re
        
        # 다양한 호스트명을 일반화
        text = re.sub(r'^[\w\-]+[>#]', 'Device# ', text, flags=re.MULTILINE)
        text = re.sub(r'^[\w\-]+\(config[^\)]*\)#', 'Device(config)# ', text, flags=re.MULTILINE)
        
        # 명령어 설명 추가 (선택적)
        command_hints = {
            'show vlan': '[VLAN 정보 조회]',
            'interface': '[인터페이스 설정]',
            'ip address': '[IP 주소 설정]',
            'switchport': '[스위치포트 설정]',
        }
        
        for cmd, hint in command_hints.items():
            if cmd in text.lower():
                text = f"{hint}\n{text}"
                break
        
        return text
    
    def compute_similarity(
        self, 
        query_embedding: np.ndarray,
        doc_embeddings: np.ndarray
    ) -> np.ndarray:
        """코사인 유사도 계산"""
        # 이미 정규화되어 있으므로 내적만 계산
        similarities = np.dot(doc_embeddings, query_embedding)
        return similarities


class HybridEmbeddingService(CiscoEmbeddingService):
    """
    하이브리드 검색을 위한 확장 서비스
    
    BGE-M3의 Dense + Sparse 임베딩 활용
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # BGE-M3 특화 설정
        if 'bge-m3' in self.model_name.lower():
            self.supports_sparse = True
        else:
            self.supports_sparse = False
    
    def embed_documents_hybrid(
        self,
        documents: List[Document]
    ) -> List[Dict]:
        """
        Dense + Sparse 하이브리드 임베딩
        """
        if not self.supports_sparse:
            logger.warning("Sparse embedding not supported. Using dense only.")
            return self.embed_documents(documents)
        
        results = []
        texts = [doc.page_content for doc in documents]
        
        # BGE-M3의 다중 표현 생성
        # 주의: sentence-transformers의 BGE-M3 구현에 따라 다를 수 있음
        try:
            outputs = self.model.encode(
                texts,
                return_dense=True,
                return_sparse=True,
                batch_size=self.batch_size
            )
            
            for i, doc in enumerate(documents):
                results.append({
                    'dense_embedding': outputs['dense_vecs'][i],
                    'sparse_embedding': outputs['lexical_weights'][i],
                    'content': doc.page_content,
                    'metadata': doc.metadata
                })
        except Exception as e:
            logger.warning(f"Hybrid encoding failed: {e}. Falling back to dense.")
            return self.embed_documents(documents)
        
        return results