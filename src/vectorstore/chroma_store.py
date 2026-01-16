# src/vectorstore/chroma_store.py

from typing import List, Dict, Optional, Any
import chromadb
from chromadb.config import Settings
from langchain_core.documents import Document
import numpy as np
import json
from pathlib import Path
import logging

from ..embedding.embedding_service import CiscoEmbeddingService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CiscoVectorStore:
    """
    시스코 매뉴얼을 위한 벡터 스토어
    
    특징:
    - ChromaDB 기반 영구 저장
    - 메타데이터 필터링 (장비 타입, 섹션 등)
    - 하이브리드 검색 지원
    """
    
    def __init__(
        self,
        collection_name: str = "cisco_manuals",
        persist_directory: str = "./vectordb",
        embedding_service: Optional[CiscoEmbeddingService] = None
    ):
        """
        Args:
            collection_name: 컬렉션 이름
            persist_directory: 영구 저장 경로
            embedding_service: 임베딩 서비스 인스턴스
        """
        self.collection_name = collection_name
        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(parents=True, exist_ok=True)
        
        # 임베딩 서비스
        self.embedding_service = embedding_service or CiscoEmbeddingService()
        
        # ChromaDB 클라이언트
        self.client = chromadb.PersistentClient(
            path=str(self.persist_directory),
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        # 컬렉션 생성/로드
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}  # 코사인 유사도
        )
        
        logger.info(f"Vector store initialized: {collection_name}")
        logger.info(f"Current document count: {self.collection.count()}")
    
    def add_documents(
        self,
        documents: List[Document],
        batch_size: int = 100
    ) -> List[str]:
        """
        문서 추가
        
        Args:
            documents: Document 리스트
            batch_size: 배치 크기
            
        Returns:
            추가된 문서 ID 리스트
        """
        all_ids = []
        
        # 배치 처리
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            
            # 임베딩 생성
            embedded_docs = self.embedding_service.embed_documents(
                batch, 
                show_progress=False
            )
            
            # ChromaDB 형식 변환
            ids = []
            embeddings = []
            metadatas = []
            contents = []
            
            for j, doc_data in enumerate(embedded_docs):
                doc_id = f"doc_{self.collection.count() + i + j}"
                
                ids.append(doc_id)
                embeddings.append(doc_data['embedding'].tolist())
                metadatas.append(self._prepare_metadata(doc_data['metadata']))
                contents.append(doc_data['content'])
            
            # 컬렉션에 추가
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                metadatas=metadatas,
                documents=contents
            )
            
            all_ids.extend(ids)
            logger.info(f"Added batch {i//batch_size + 1}: {len(batch)} documents")
        
        logger.info(f"Total documents added: {len(all_ids)}")
        return all_ids
    
    def _prepare_metadata(self, metadata: Dict) -> Dict:
        """메타데이터 정리 (ChromaDB 호환)"""
        clean_metadata = {}
        
        for key, value in metadata.items():
            # ChromaDB는 기본 타입만 지원
            if isinstance(value, (str, int, float, bool)):
                clean_metadata[key] = value
            elif isinstance(value, list):
                clean_metadata[key] = json.dumps(value)
            else:
                clean_metadata[key] = str(value)
        
        return clean_metadata
    
    def search(
        self,
        query: str,
        k: int = 5,
        filter_metadata: Optional[Dict] = None
    ) -> List[Dict]:
        """
        유사도 검색
        
        Args:
            query: 검색 쿼리
            k: 반환할 문서 수
            filter_metadata: 메타데이터 필터 (예: {"device": "Catalyst 9000"})
            
        Returns:
            검색 결과 리스트
        """
        # 쿼리 임베딩
        query_embedding = self.embedding_service.embed_query(query)
        
        # 검색 실행
        where_filter = self._build_where_filter(filter_metadata)
        
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            where=where_filter,
            include=["documents", "metadatas", "distances"]
        )
        
        # 결과 정리
        search_results = []
        
        if results['documents'] and results['documents'][0]:
            for i, (doc, metadata, distance) in enumerate(zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            )):
                search_results.append({
                    'content': doc,
                    'metadata': metadata,
                    'score': 1 - distance,  # distance를 similarity로 변환
                    'rank': i + 1
                })
        
        return search_results
    
    def _build_where_filter(self, filter_metadata: Optional[Dict]) -> Optional[Dict]:
        """ChromaDB where 필터 생성"""
        if not filter_metadata:
            return None
        
        conditions = []
        for key, value in filter_metadata.items():
            conditions.append({key: {"$eq": value}})
        
        if len(conditions) == 1:
            return conditions[0]
        return {"$and": conditions}
    
    def search_by_section(
        self,
        query: str,
        section: str,
        k: int = 5
    ) -> List[Dict]:
        """섹션별 검색"""
        return self.search(
            query=query,
            k=k,
            filter_metadata={"section": section}
        )
    
    def search_cli_commands(
        self,
        query: str,
        k: int = 5
    ) -> List[Dict]:
        """CLI 명령어만 검색"""
        return self.search(
            query=query,
            k=k,
            filter_metadata={"chunk_type": "cli_command"}
        )
    
    def get_collection_stats(self) -> Dict:
        """컬렉션 통계"""
        count = self.collection.count()
        
        # 샘플 메타데이터로 구조 파악
        if count > 0:
            sample = self.collection.peek(limit=10)
            metadata_keys = set()
            chunk_types = set()
            
            for meta in sample['metadatas']:
                metadata_keys.update(meta.keys())
                if 'chunk_type' in meta:
                    chunk_types.add(meta['chunk_type'])
        else:
            metadata_keys = set()
            chunk_types = set()
        
        return {
            'total_documents': count,
            'metadata_fields': list(metadata_keys),
            'chunk_types': list(chunk_types),
            'persist_directory': str(self.persist_directory)
        }
    
    def delete_collection(self):
        """컬렉션 삭제"""
        self.client.delete_collection(self.collection_name)
        logger.info(f"Collection deleted: {self.collection_name}")
    
    def reset(self):
        """전체 초기화"""
        self.client.reset()
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        logger.info("Vector store reset complete")