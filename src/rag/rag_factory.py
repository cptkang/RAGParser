# src/rag/rag_factory.py

from typing import Optional, Dict, Any
from enum import Enum

from .rag_chain import CiscoRAGChain, ReRankingRAGChain
from .advanced_rag import (
    HybridSearchRAG,
    ConversationalRAG,
    StepByStepRAG,
    TroubleshootingRAG,
    SummaryRAG,
    ComparisonRAG
)
from ..vectorstore.chroma_store import CiscoVectorStore
from ..llm.llama_service import BaseLlamaService, OllamaService


class RAGMode(Enum):
    """RAG 모드 정의"""
    DEFAULT = "default"
    HYBRID = "hybrid"
    CONVERSATIONAL = "conversational"
    STEP_BY_STEP = "stepbystep"
    TROUBLESHOOTING = "troubleshooting"
    SUMMARY = "summary"
    COMPARISON = "comparison"
    RERANKING = "reranking"


class RAGFactory:
    """
    RAG 체인 팩토리
    
    다양한 RAG 모드에 따른 적절한 체인 생성
    """
    
    def __init__(
        self,
        vector_store: CiscoVectorStore,
        llm_service: Optional[BaseLlamaService] = None,
        default_top_k: int = 5,
        default_score_threshold: float = 0.5
    ):
        """
        Args:
            vector_store: 벡터 스토어
            llm_service: LLM 서비스
            default_top_k: 기본 검색 문서 수
            default_score_threshold: 기본 유사도 임계값
        """
        self.vector_store = vector_store
        self.llm_service = llm_service or OllamaService()
        self.default_top_k = default_top_k
        self.default_score_threshold = default_score_threshold
        
        # 캐시된 체인
        self._chains: Dict[RAGMode, CiscoRAGChain] = {}
    
    def get_chain(
        self,
        mode: RAGMode = RAGMode.DEFAULT,
        **kwargs
    ) -> CiscoRAGChain:
        """
        지정된 모드의 RAG 체인 반환
        
        Args:
            mode: RAG 모드
            **kwargs: 추가 설정
            
        Returns:
            RAG 체인 인스턴스
        """
        # 대화형은 세션별로 별도 생성 필요
        if mode == RAGMode.CONVERSATIONAL:
            return self._create_chain(mode, **kwargs)
        
        # 캐시 확인
        if mode not in self._chains:
            self._chains[mode] = self._create_chain(mode, **kwargs)
        
        return self._chains[mode]
    
    def _create_chain(
        self,
        mode: RAGMode,
        **kwargs
    ) -> CiscoRAGChain:
        """
        RAG 체인 생성
        
        Args:
            mode: RAG 모드
            **kwargs: 추가 설정
            
        Returns:
            RAG 체인 인스턴스
        """
        base_config = {
            'vector_store': self.vector_store,
            'llm_service': self.llm_service,
            'top_k': kwargs.get('top_k', self.default_top_k),
            'score_threshold': kwargs.get('score_threshold', self.default_score_threshold)
        }
        
        chain_classes = {
            RAGMode.DEFAULT: CiscoRAGChain,
            RAGMode.HYBRID: HybridSearchRAG,
            RAGMode.CONVERSATIONAL: ConversationalRAG,
            RAGMode.STEP_BY_STEP: StepByStepRAG,
            RAGMode.TROUBLESHOOTING: TroubleshootingRAG,
            RAGMode.SUMMARY: SummaryRAG,
            RAGMode.COMPARISON: ComparisonRAG,
            RAGMode.RERANKING: ReRankingRAGChain,
        }
        
        chain_class = chain_classes.get(mode, CiscoRAGChain)
        
        # 모드별 추가 설정
        if mode == RAGMode.HYBRID:
            base_config['keyword_weight'] = kwargs.get('keyword_weight', 0.3)
        elif mode == RAGMode.CONVERSATIONAL:
            base_config['max_history'] = kwargs.get('max_history', 5)
        elif mode == RAGMode.RERANKING:
            base_config['rerank_top_k'] = kwargs.get('rerank_top_k', 3)
        
        return chain_class(**base_config)
    
    def auto_select_mode(self, question: str) -> RAGMode:
        """
        질문에 따른 자동 모드 선택
        
        Args:
            question: 사용자 질문
            
        Returns:
            추천 RAG 모드
        """
        question_lower = question.lower()
        
        # 트러블슈팅 패턴
        troubleshoot_patterns = [
            '안됨', '안되', '문제', '오류', '에러', 'error', 'fail',
            '왜', '원인', '해결', 'trouble', 'issue', 'problem', '안됩'
        ]
        if any(p in question_lower for p in troubleshoot_patterns):
            return RAGMode.TROUBLESHOOTING
        
        # 절차/설정 패턴
        procedure_patterns = [
            '방법', '절차', '단계', '설정', '구성', '하는법',
            'how to', 'configure', 'setup', 'create'
        ]
        if any(p in question_lower for p in procedure_patterns):
            return RAGMode.STEP_BY_STEP
        
        # 비교 패턴
        comparison_patterns = ['비교', '차이', 'vs', '다른점', '장단점']
        if any(p in question_lower for p in comparison_patterns):
            return RAGMode.COMPARISON
        
        # 요약 패턴
        summary_patterns = ['요약', '정리', '개요', '설명해', 'summary']
        if any(p in question_lower for p in summary_patterns):
            return RAGMode.SUMMARY
        
        # 기본값: 하이브리드 검색
        return RAGMode.HYBRID


class UnifiedRAGInterface:
    """
    통합 RAG 인터페이스
    
    단일 인터페이스로 모든 RAG 기능 제공
    """
    
    def __init__(
        self,
        vector_store: CiscoVectorStore,
        llm_service: Optional[BaseLlamaService] = None
    ):
        self.factory = RAGFactory(
            vector_store=vector_store,
            llm_service=llm_service
        )
        self._conversation_sessions: Dict[str, ConversationalRAG] = {}
    
    def query(
        self,
        question: str,
        mode: Optional[str] = None,
        auto_mode: bool = True,
        **kwargs
    ):
        """
        통합 쿼리 인터페이스
        
        Args:
            question: 질문
            mode: RAG 모드 (문자열)
            auto_mode: 자동 모드 선택 여부
            **kwargs: 추가 옵션
            
        Returns:
            RAGResponse
        """
        # 모드 결정
        if mode:
            rag_mode = RAGMode(mode)
        elif auto_mode:
            rag_mode = self.factory.auto_select_mode(question)
        else:
            rag_mode = RAGMode.DEFAULT
        
        # 체인 가져오기
        chain = self.factory.get_chain(rag_mode, **kwargs)
        
        # 쿼리 실행
        return chain.query(question, **kwargs)
    
    def conversation(
        self,
        question: str,
        session_id: str,
        **kwargs
    ):
        """
        대화형 쿼리
        
        Args:
            question: 질문
            session_id: 세션 ID
            **kwargs: 추가 옵션
            
        Returns:
            RAGResponse
        """
        if session_id not in self._conversation_sessions:
            self._conversation_sessions[session_id] = self.factory.get_chain(
                RAGMode.CONVERSATIONAL,
                **kwargs
            )
        
        return self._conversation_sessions[session_id].query(question, **kwargs)
    
    def clear_session(self, session_id: str):
        """세션 초기화"""
        if session_id in self._conversation_sessions:
            self._conversation_sessions[session_id].clear_history()
    
    def delete_session(self, session_id: str):
        """세션 삭제"""
        if session_id in self._conversation_sessions:
            del self._conversation_sessions[session_id]
    
    def compare(self, item1: str, item2: str, aspect: Optional[str] = None):
        """
        비교 쿼리
        
        Args:
            item1: 첫 번째 항목
            item2: 두 번째 항목
            aspect: 비교 관점
            
        Returns:
            RAGResponse
        """
        chain = self.factory.get_chain(RAGMode.COMPARISON)
        return chain.compare(item1, item2, aspect)
    
    def summarize(self, topic: str, **kwargs):
        """
        요약 쿼리
        
        Args:
            topic: 요약 주제
            **kwargs: 추가 옵션
            
        Returns:
            RAGResponse
        """
        chain = self.factory.get_chain(RAGMode.SUMMARY)
        return chain.summarize_topic(topic, **kwargs)
    
    def troubleshoot(self, problem: str, **kwargs):
        """
        트러블슈팅 쿼리
        
        Args:
            problem: 문제 설명
            **kwargs: 추가 옵션
            
        Returns:
            RAGResponse
        """
        chain = self.factory.get_chain(RAGMode.TROUBLESHOOTING)
        return chain.query(problem, **kwargs)