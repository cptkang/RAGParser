# src/embedding/dual_embedding_service.py

"""
이중 임베딩 서비스

영문 문서용 모델과 한국어 쿼리용 모델을 분리하여 최적 성능 달성
"""

from typing import List, Dict, Optional, Union
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document
import torch
import logging

from .model_selection import (
    select_document_model,
    select_query_model,
    select_unified_model,
    EmbeddingModelInfo,
    ENGLISH_DOCUMENT_MODELS
)
from .offline_utils import auto_detect_local_files_only, get_offline_strategy_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DualEmbeddingService:
    """
    이중 임베딩 서비스

    특징:
    - 영문 문서: 영문 특화 모델 (BGE-Large-EN-v1.5)
    - 한국어 쿼리: 번역 후 동일 모델 사용
    - 최고 성능 달성
    """

    def __init__(
        self,
        document_model: Optional[str] = None,
        device: Optional[str] = None,
        batch_size: int = 32,
        local_files_only: Optional[bool] = None,
        trust_remote_code: bool = False
    ):
        """
        Args:
            document_model: 문서 임베딩 모델 (None이면 자동 선택)
            device: cuda/cpu
            batch_size: 배치 크기
            local_files_only: 오프라인 모드 (None이면 자동 감지, True/False로 명시 가능)
            trust_remote_code: 원격 코드 실행 허용 여부
        """
        import os

        # 디바이스 설정
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.batch_size = batch_size

        # 오프라인 모드 자동 감지
        self.local_files_only = auto_detect_local_files_only(local_files_only)

        # 오프라인 모드일 경우 환경 변수 설정 (HuggingFace Hub 접근 차단)
        if self.local_files_only:
            os.environ['HF_HUB_OFFLINE'] = '1'
            os.environ['TRANSFORMERS_OFFLINE'] = '1'
            logger.info("환경 변수 설정: HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1")

        # 문서 모델 선택
        if document_model is None:
            model_info = select_document_model()
            document_model = model_info.model_id
            logger.info(f"Auto-selected document model: {model_info.name}")

        self.document_model_name = document_model

        # 영문 문서용 모델 로드
        logger.info(f"Loading document model: {document_model}")
        logger.info(f"Device: {self.device}")
        logger.info(f"Offline mode: {self.local_files_only}")

        try:
            self.document_model = SentenceTransformer(
                document_model,
                device=self.device,
                local_files_only=self.local_files_only,
                trust_remote_code=trust_remote_code
            )
        except Exception as e:
            if self.local_files_only:
                logger.error(
                    f"오프라인 모드에서 모델을 로드할 수 없습니다.\n"
                    f"{get_offline_strategy_message()}"
                )
            raise e

        self.dimension = self.document_model.get_sentence_embedding_dimension()
        logger.info(f"Embedding dimension: {self.dimension}")

        # E5 모델 체크
        self.use_prefix = 'e5' in document_model.lower()
        if self.use_prefix:
            logger.info("E5 model detected. Using query:/passage: prefix")

    def embed_documents(
        self,
        documents: List[Document],
        show_progress: bool = True
    ) -> List[Dict]:
        """
        영문 문서 임베딩

        Args:
            documents: Document 리스트
            show_progress: 진행 상황 표시

        Returns:
            임베딩 결과
        """
        results = []
        texts = []

        for doc in documents:
            text = doc.page_content

            # CLI 명령어 전처리
            if doc.metadata.get('chunk_type') == 'cli_command':
                text = self._preprocess_cli(text)

            # E5 프리픽스
            if self.use_prefix:
                text = "passage: " + text

            texts.append(text)

        # 배치 임베딩
        embeddings = self.document_model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            batch_size=self.batch_size,
            show_progress_bar=show_progress
        )

        for doc, embedding in zip(documents, embeddings):
            results.append({
                'embedding': embedding,
                'content': doc.page_content,
                'metadata': doc.metadata
            })

        return results

    def embed_query(
        self,
        query: str,
        language: str = "en"
    ) -> np.ndarray:
        """
        쿼리 임베딩

        Args:
            query: 검색 쿼리 (이미 영어로 번역된 상태)
            language: 쿼리 언어 (현재는 항상 'en' - 번역 후 사용)

        Returns:
            쿼리 임베딩 벡터
        """
        # 번역된 영어 쿼리를 문서 모델로 임베딩
        if self.use_prefix:
            query = "query: " + query

        embedding = self.document_model.encode(
            query,
            normalize_embeddings=True,
            convert_to_numpy=True
        )

        return embedding

    def embed_queries(self, queries: List[str]) -> np.ndarray:
        """다중 쿼리 임베딩"""
        if self.use_prefix:
            queries = ["query: " + q for q in queries]

        embeddings = self.document_model.encode(
            queries,
            normalize_embeddings=True,
            convert_to_numpy=True,
            batch_size=self.batch_size
        )

        return embeddings

    def _preprocess_cli(self, text: str) -> str:
        """CLI 명령어 전처리"""
        import re

        # 프롬프트 정규화
        text = re.sub(r'^[\w\-]+[>#]', 'Device# ', text, flags=re.MULTILINE)
        text = re.sub(
            r'^[\w\-]+\(config[^\)]*\)#',
            'Device(config)# ',
            text,
            flags=re.MULTILINE
        )

        # 주요 명령어 힌트
        command_hints = {
            'show': '[Display information]',
            'configure': '[Enter configuration mode]',
            'interface': '[Configure interface]',
            'vlan': '[VLAN configuration]',
            'ip address': '[Set IP address]',
            'switchport': '[Configure switchport]',
            'router': '[Router configuration]',
            'spanning-tree': '[STP configuration]',
        }

        text_lower = text.lower()
        for cmd, hint in command_hints.items():
            if cmd in text_lower:
                text = f"{hint}\n{text}"
                break

        return text

    def compute_similarity(
        self,
        query_embedding: np.ndarray,
        doc_embeddings: np.ndarray
    ) -> np.ndarray:
        """코사인 유사도 계산"""
        similarities = np.dot(doc_embeddings, query_embedding)
        return similarities

    def get_model_info(self) -> Dict:
        """모델 정보 반환"""
        return {
            'document_model': self.document_model_name,
            'dimension': self.dimension,
            'device': self.device,
            'use_prefix': self.use_prefix
        }


class UnifiedEmbeddingService:
    """
    통합 임베딩 서비스

    하나의 다국어 모델로 문서와 쿼리 모두 처리
    """

    def __init__(
        self,
        model_name: Optional[str] = None,
        device: Optional[str] = None,
        batch_size: int = 32,
        local_files_only: Optional[bool] = None,
        trust_remote_code: bool = False
    ):
        """
        Args:
            model_name: 모델명 (None이면 자동 선택)
            device: cuda/cpu
            batch_size: 배치 크기
            local_files_only: 오프라인 모드 (None이면 자동 감지, True/False로 명시 가능)
            trust_remote_code: 원격 코드 실행 허용 여부
        """
        import os

        # 디바이스 설정
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.batch_size = batch_size

        # 오프라인 모드 자동 감지
        self.local_files_only = auto_detect_local_files_only(local_files_only)

        # 오프라인 모드일 경우 환경 변수 설정 (HuggingFace Hub 접근 차단)
        if self.local_files_only:
            os.environ['HF_HUB_OFFLINE'] = '1'
            os.environ['TRANSFORMERS_OFFLINE'] = '1'
            logger.info("환경 변수 설정: HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1")

        # 모델 선택
        if model_name is None:
            model_info = select_unified_model()
            model_name = model_info.model_id
            logger.info(f"Auto-selected unified model: {model_info.name}")

        self.model_name = model_name

        # 모델 로드
        logger.info(f"Loading unified model: {model_name}")
        logger.info(f"Device: {self.device}")
        logger.info(f"Offline mode: {self.local_files_only}")

        try:
            self.model = SentenceTransformer(
                model_name,
                device=self.device,
                local_files_only=self.local_files_only,
                trust_remote_code=trust_remote_code
            )
        except Exception as e:
            if self.local_files_only:
                logger.error(
                    f"오프라인 모드에서 모델을 로드할 수 없습니다.\n"
                    f"{get_offline_strategy_message()}"
                )
            raise e

        self.dimension = self.model.get_sentence_embedding_dimension()
        logger.info(f"Embedding dimension: {self.dimension}")

        # E5 모델 체크
        self.use_prefix = 'e5' in model_name.lower()

    def embed_documents(
        self,
        documents: List[Document],
        show_progress: bool = True
    ) -> List[Dict]:
        """문서 임베딩"""
        results = []
        texts = []

        for doc in documents:
            text = doc.page_content

            if doc.metadata.get('chunk_type') == 'cli_command':
                text = self._preprocess_cli(text)

            if self.use_prefix:
                text = "passage: " + text

            texts.append(text)

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            batch_size=self.batch_size,
            show_progress_bar=show_progress
        )

        for doc, embedding in zip(documents, embeddings):
            results.append({
                'embedding': embedding,
                'content': doc.page_content,
                'metadata': doc.metadata
            })

        return results

    def embed_query(self, query: str, language: str = "auto") -> np.ndarray:
        """쿼리 임베딩"""
        if self.use_prefix:
            query = "query: " + query

        embedding = self.model.encode(
            query,
            normalize_embeddings=True,
            convert_to_numpy=True
        )

        return embedding

    def embed_queries(self, queries: List[str]) -> np.ndarray:
        """다중 쿼리 임베딩"""
        if self.use_prefix:
            queries = ["query: " + q for q in queries]

        embeddings = self.model.encode(
            queries,
            normalize_embeddings=True,
            convert_to_numpy=True,
            batch_size=self.batch_size
        )

        return embeddings

    def _preprocess_cli(self, text: str) -> str:
        """CLI 명령어 전처리"""
        import re

        text = re.sub(r'^[\w\-]+[>#]', 'Device# ', text, flags=re.MULTILINE)
        text = re.sub(
            r'^[\w\-]+\(config[^\)]*\)#',
            'Device(config)# ',
            text,
            flags=re.MULTILINE
        )

        return text

    def compute_similarity(
        self,
        query_embedding: np.ndarray,
        doc_embeddings: np.ndarray
    ) -> np.ndarray:
        """코사인 유사도 계산"""
        similarities = np.dot(doc_embeddings, query_embedding)
        return similarities

    def get_model_info(self) -> Dict:
        """모델 정보 반환"""
        return {
            'model': self.model_name,
            'dimension': self.dimension,
            'device': self.device,
            'use_prefix': self.use_prefix
        }


def create_embedding_service(
    strategy: str = "dual",
    document_model: Optional[str] = None,
    device: Optional[str] = None,
    batch_size: int = 32,
    local_files_only: Optional[bool] = None,
    trust_remote_code: bool = False
) -> Union[DualEmbeddingService, UnifiedEmbeddingService]:
    """
    임베딩 서비스 팩토리

    Args:
        strategy: 'dual' (분리) 또는 'unified' (통합)
        document_model: 모델명
        device: 디바이스
        batch_size: 배치 크기
        local_files_only: 오프라인 모드 (None이면 자동 감지)
        trust_remote_code: 원격 코드 실행 허용

    Returns:
        임베딩 서비스 인스턴스
    """
    if strategy == "dual":
        logger.info("Creating dual embedding service (separate models)")
        return DualEmbeddingService(
            document_model=document_model,
            device=device,
            batch_size=batch_size,
            local_files_only=local_files_only,
            trust_remote_code=trust_remote_code
        )
    elif strategy == "unified":
        logger.info("Creating unified embedding service (single model)")
        return UnifiedEmbeddingService(
            model_name=document_model,
            device=device,
            batch_size=batch_size,
            local_files_only=local_files_only,
            trust_remote_code=trust_remote_code
        )
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
