# src/rag/rag_chain.py

from typing import List, Dict, Optional, Generator
from dataclasses import dataclass
import logging

from ..vectorstore.chroma_store import CiscoVectorStore
from ..llm.llama_service import BaseLlamaService, OllamaService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class RAGResponse:
    """RAG 응답 데이터"""
    answer: str
    sources: List[Dict]
    query: str
    confidence: float


class CiscoRAGChain:
    """
    시스코 네트워크 매뉴얼 RAG 체인
    
    특징:
    - 컨텍스트 기반 프롬프트 템플릿
    - CLI 명령어 포맷팅
    - 소스 인용
    - 신뢰도 평가
    """
    
    # 시스코 매뉴얼 특화 시스템 프롬프트
    SYSTEM_PROMPT = """당신은 시스코 네트워크 장비 전문가입니다. 
제공된 매뉴얼 컨텍스트를 기반으로 정확하고 실용적인 답변을 제공합니다.

답변 지침:
1. 제공된 컨텍스트 정보만 사용하여 답변하세요.
2. CLI 명령어를 포함할 때는 정확한 구문을 사용하세요.
3. 단계별 절차가 필요한 경우 명확히 구분하여 설명하세요.
4. 컨텍스트에 정보가 없으면 "제공된 문서에서 해당 정보를 찾을 수 없습니다"라고 답하세요.
5. 관련 주의사항이나 경고가 있다면 반드시 포함하세요.

답변은 한국어로 작성하되, 명령어와 기술 용어는 원어 그대로 사용하세요."""

    # RAG 프롬프트 템플릿
    RAG_TEMPLATE = """다음 컨텍스트를 참고하여 질문에 답변하세요.

### 컨텍스트:
{context}

### 질문:
{question}

### 답변:"""

    def __init__(
        self,
        vector_store: CiscoVectorStore,
        llm_service: Optional[BaseLlamaService] = None,
        top_k: int = 5,
        score_threshold: float = 0.5
    ):
        """
        Args:
            vector_store: 벡터 스토어 인스턴스
            llm_service: LLM 서비스 인스턴스
            top_k: 검색할 문서 수
            score_threshold: 최소 유사도 점수
        """
        self.vector_store = vector_store
        self.llm_service = llm_service or OllamaService()
        self.top_k = top_k
        self.score_threshold = score_threshold
    
    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> RAGResponse:
        """
        RAG 쿼리 실행
        
        Args:
            question: 사용자 질문
            filter_metadata: 메타데이터 필터
            include_sources: 소스 포함 여부
            
        Returns:
            RAGResponse 객체
        """
        # 1. 관련 문서 검색
        search_results = self.vector_store.search(
            query=question,
            k=self.top_k,
            filter_metadata=filter_metadata
        )
        
        # 2. 점수 기준 필터링
        relevant_docs = [
            doc for doc in search_results 
            if doc['score'] >= self.score_threshold
        ]
        
        if not relevant_docs:
            return RAGResponse(
                answer="제공된 문서에서 관련 정보를 찾을 수 없습니다. 다른 키워드로 검색해 주세요.",
                sources=[],
                query=question,
                confidence=0.0
            )
        
        # 3. 컨텍스트 구성
        context = self._build_context(relevant_docs)
        
        # 4. 프롬프트 생성
        prompt = self.RAG_TEMPLATE.format(
            context=context,
            question=question
        )
        
        # 5. LLM 응답 생성
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        )
        
        # 6. 신뢰도 계산
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs if include_sources else [],
            query=question,
            confidence=confidence
        )
    
    def query_stream(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None
    ) -> Generator[str, None, None]:
        """
        스트리밍 RAG 쿼리
        
        Args:
            question: 사용자 질문
            filter_metadata: 메타데이터 필터
            
        Yields:
            응답 토큰
        """
        # 문서 검색
        search_results = self.vector_store.search(
            query=question,
            k=self.top_k,
            filter_metadata=filter_metadata
        )
        
        relevant_docs = [
            doc for doc in search_results 
            if doc['score'] >= self.score_threshold
        ]
        
        if not relevant_docs:
            yield "제공된 문서에서 관련 정보를 찾을 수 없습니다."
            return
        
        # 컨텍스트 및 프롬프트 구성
        context = self._build_context(relevant_docs)
        prompt = self.RAG_TEMPLATE.format(
            context=context,
            question=question
        )
        
        # 스트리밍 응답
        for token in self.llm_service.generate_stream(
            prompt=prompt,
            system_prompt=self.SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        ):
            yield token
    
    def _build_context(self, docs: List[Dict]) -> str:
        """
        검색된 문서들로 컨텍스트 구성
        
        Args:
            docs: 검색된 문서 리스트
            
        Returns:
            포맷팅된 컨텍스트 문자열
        """
        context_parts = []
        
        for i, doc in enumerate(docs, 1):
            # 메타데이터 헤더
            metadata = doc.get('metadata', {})
            source_info = []
            
            if metadata.get('chapter'):
                source_info.append(f"챕터: {metadata['chapter']}")
            if metadata.get('section'):
                source_info.append(f"섹션: {metadata['section']}")
            if metadata.get('chunk_type') == 'cli_command':
                source_info.append("[CLI 명령어]")
            
            header = f"[문서 {i}] " + " | ".join(source_info) if source_info else f"[문서 {i}]"
            
            # 컨텍스트 내용
            content = doc['content']
            
            # CLI 명령어 포맷팅
            if metadata.get('chunk_type') == 'cli_command':
                content = self._format_cli_block(content)
            
            context_parts.append(f"{header}\n{content}")
        
        return "\n\n---\n\n".join(context_parts)
    
    def _format_cli_block(self, content: str) -> str:
        """
        CLI 블록 포맷팅
        
        Args:
            content: CLI 명령어 내용
            
        Returns:
            포맷팅된 CLI 블록
        """
        lines = content.strip().split('\n')
        formatted_lines = []
        
        for line in lines:
            # 프롬프트 라인 강조
            if any(indicator in line for indicator in ['#', '>', '(config']):
                formatted_lines.append(f"  {line}")
            else:
                formatted_lines.append(f"    {line}")
        
        return "```\n" + "\n".join(formatted_lines) + "\n```"
    
    def _calculate_confidence(
        self, 
        docs: List[Dict], 
        answer: str
    ) -> float:
        """
        응답 신뢰도 계산
        
        기준:
        - 검색된 문서 유사도 점수
        - 문서 개수
        - 응답 품질 휴리스틱
        
        Args:
            docs: 검색된 문서 리스트
            answer: 생성된 답변
            
        Returns:
            0.0 ~ 1.0 사이의 신뢰도 점수
        """
        if not docs:
            return 0.0
        
        # 평균 유사도 점수
        avg_score = sum(d['score'] for d in docs) / len(docs)
        
        # 문서 개수 보너스 (최대 3개까지)
        doc_bonus = min(len(docs) / 3, 1.0) * 0.2
        
        # 응답 품질 체크 (간단한 휴리스틱)
        quality_score = 0.0
        
        # CLI 명령어가 포함된 경우 가산점
        if '```' in answer or '#' in answer:
            quality_score += 0.1
        
        # 적절한 길이
        if 50 < len(answer) < 2000:
            quality_score += 0.1
        
        # "찾을 수 없습니다" 같은 부정적 응답 감점
        negative_phrases = ["찾을 수 없", "없습니다", "모르겠", "확인되지"]
        if any(phrase in answer for phrase in negative_phrases):
            quality_score -= 0.2
        
        # 최종 신뢰도
        confidence = min(avg_score * 0.6 + doc_bonus + quality_score, 1.0)
        confidence = max(confidence, 0.0)  # 음수 방지
        
        return round(confidence, 3)
    
    def query_cli_command(
        self,
        command_description: str
    ) -> RAGResponse:
        """
        CLI 명령어 전용 검색
        
        Args:
            command_description: 명령어 설명 또는 검색어
            
        Returns:
            RAGResponse 객체
        """
        return self.query(
            question=command_description,
            filter_metadata={"chunk_type": "cli_command"}
        )
    
    def query_by_device(
        self,
        question: str,
        device_type: str
    ) -> RAGResponse:
        """
        특정 장비 타입으로 필터링된 검색
        
        Args:
            question: 사용자 질문
            device_type: 장비 타입 (예: "Catalyst 9000")
            
        Returns:
            RAGResponse 객체
        """
        return self.query(
            question=question,
            filter_metadata={"device_type": device_type}
        )
    
    def query_by_section(
        self,
        question: str,
        section: str
    ) -> RAGResponse:
        """
        특정 섹션으로 필터링된 검색
        
        Args:
            question: 사용자 질문
            section: 섹션 이름
            
        Returns:
            RAGResponse 객체
        """
        return self.query(
            question=question,
            filter_metadata={"section": section}
        )
    
    def multi_query(
        self,
        question: str,
        query_variations: Optional[List[str]] = None
    ) -> RAGResponse:
        """
        다중 쿼리 RAG - 여러 변형 질문으로 검색 후 통합
        
        Args:
            question: 원본 질문
            query_variations: 질문 변형 리스트 (없으면 자동 생성)
            
        Returns:
            통합된 RAGResponse
        """
        # 질문 변형 생성
        if query_variations is None:
            query_variations = self._generate_query_variations(question)
        
        all_queries = [question] + query_variations
        
        # 모든 쿼리로 문서 검색
        all_docs = {}
        for q in all_queries:
            results = self.vector_store.search(query=q, k=self.top_k)
            for doc in results:
                doc_id = doc['content'][:100]  # 간단한 ID
                if doc_id not in all_docs or doc['score'] > all_docs[doc_id]['score']:
                    all_docs[doc_id] = doc
        
        # 점수순 정렬 및 상위 선택
        sorted_docs = sorted(
            all_docs.values(), 
            key=lambda x: x['score'], 
            reverse=True
        )[:self.top_k]
        
        # 필터링
        relevant_docs = [
            doc for doc in sorted_docs 
            if doc['score'] >= self.score_threshold
        ]
        
        if not relevant_docs:
            return RAGResponse(
                answer="제공된 문서에서 관련 정보를 찾을 수 없습니다.",
                sources=[],
                query=question,
                confidence=0.0
            )
        
        # 컨텍스트 및 응답 생성
        context = self._build_context(relevant_docs)
        prompt = self.RAG_TEMPLATE.format(context=context, question=question)
        
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        )
        
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs,
            query=question,
            confidence=confidence
        )
    
    def _generate_query_variations(self, question: str) -> List[str]:
        """
        질문 변형 자동 생성
        
        Args:
            question: 원본 질문
            
        Returns:
            변형된 질문 리스트
        """
        variation_prompt = f"""다음 질문에 대해 같은 의미의 다른 표현 2개를 생성하세요.
기술 용어는 유지하고, 문장 구조만 변경하세요.

원본 질문: {question}

변형 1:
변형 2:"""

        try:
            response = self.llm_service.generate(
                prompt=variation_prompt,
                max_tokens=200,
                temperature=0.7
            )
            
            # 파싱
            lines = response.strip().split('\n')
            variations = []
            for line in lines:
                if line.strip() and not line.startswith('변형'):
                    variations.append(line.strip())
            
            return variations[:2]
        except Exception as e:
            logger.warning(f"Query variation generation failed: {e}")
            return []


class ReRankingRAGChain(CiscoRAGChain):
    """
    Re-Ranking을 적용한 RAG 체인
    
    1차 검색 후 LLM 기반 재순위화 수행
    """
    
    RERANK_PROMPT = """다음 문서들이 질문에 얼마나 관련있는지 1-10점으로 평가하세요.

질문: {question}

문서들:
{documents}

각 문서에 대해 다음 형식으로 점수를 매기세요:
문서1: [점수]
문서2: [점수]
...

점수만 출력하세요:"""

    def __init__(
        self,
        *args,
        rerank_top_k: int = 3,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.rerank_top_k = rerank_top_k
    
    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> RAGResponse:
        """
        Re-Ranking 적용 RAG 쿼리
        """
        # 1. 1차 검색 (더 많이)
        search_results = self.vector_store.search(
            query=question,
            k=self.top_k * 2,
            filter_metadata=filter_metadata
        )
        
        if not search_results:
            return RAGResponse(
                answer="관련 문서를 찾을 수 없습니다.",
                sources=[],
                query=question,
                confidence=0.0
            )
        
        # 2. Re-Ranking
        reranked_docs = self._rerank_documents(question, search_results)
        
        # 3. 상위 문서 선택
        relevant_docs = reranked_docs[:self.rerank_top_k]
        
        # 4. 응답 생성
        context = self._build_context(relevant_docs)
        prompt = self.RAG_TEMPLATE.format(context=context, question=question)
        
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        )
        
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs if include_sources else [],
            query=question,
            confidence=confidence
        )
    
    def _rerank_documents(
        self,
        question: str,
        documents: List[Dict]
    ) -> List[Dict]:
        """
        문서 재순위화
        
        Args:
            question: 질문
            documents: 검색된 문서 리스트
            
        Returns:
            재순위화된 문서 리스트
        """
        # 문서 요약 준비
        doc_summaries = []
        for i, doc in enumerate(documents, 1):
            content = doc['content'][:300]  # 처음 300자만
            doc_summaries.append(f"문서{i}: {content}")
        
        documents_text = "\n\n".join(doc_summaries)
        
        prompt = self.RERANK_PROMPT.format(
            question=question,
            documents=documents_text
        )
        
        try:
            response = self.llm_service.generate(
                prompt=prompt,
                max_tokens=100,
                temperature=0.0
            )
            
            # 점수 파싱
            scores = self._parse_rerank_scores(response, len(documents))
            
            # 점수와 함께 정렬
            for i, doc in enumerate(documents):
                doc['rerank_score'] = scores.get(i, 0)
            
            documents.sort(key=lambda x: x.get('rerank_score', 0), reverse=True)
            
        except Exception as e:
            logger.warning(f"Reranking failed: {e}. Using original order.")
        
        return documents
    
    def _parse_rerank_scores(
        self,
        response: str,
        num_docs: int
    ) -> Dict[int, float]:
        """
        Re-Ranking 응답에서 점수 파싱
        
        Args:
            response: LLM 응답
            num_docs: 문서 수
            
        Returns:
            {문서인덱스: 점수} 딕셔너리
        """
        import re
        
        scores = {}
        
        # "문서1: 8" 또는 "1: 8" 패턴 매칭
        patterns = [
            r'문서(\d+):\s*(\d+(?:\.\d+)?)',
            r'(\d+):\s*(\d+(?:\.\d+)?)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, response)
            for match in matches:
                idx = int(match[0]) - 1  # 0-based index
                score = float(match[1])
                if 0 <= idx < num_docs:
                    scores[idx] = score
        
        return scores