# src/rag/advanced_rag.py

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import re
import logging
from collections import defaultdict

from .rag_chain import CiscoRAGChain, RAGResponse
from ..vectorstore.chroma_store import CiscoVectorStore
from ..llm.llama_service import BaseLlamaService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HybridSearchRAG(CiscoRAGChain):
    """
    하이브리드 검색 (Dense + Keyword) RAG
    
    시스코 매뉴얼의 특성:
    - CLI 명령어: 정확한 키워드 매칭 중요
    - 개념 설명: 의미 기반 검색 중요
    """
    
    # 시스코 관련 키워드 패턴
    CISCO_KEYWORD_PATTERNS = [
        r'\b(show|configure|interface|vlan|ip|router|switch)\b',
        r'\b(VLAN|OSPF|BGP|EIGRP|STP|RSTP|PVST|ACL|QoS)\b',
        r'\b(Gi\d+/\d+|Fa\d+/\d+|Te\d+/\d+|Eth\d+/\d+)\b',
        r'\b(trunk|access|native|allowed|spanning-tree)\b',
        r'\b(enable|disable|shutdown|no\s+shutdown)\b',
        r'\b(config|configuration|설정|구성)\b',
        r'\b(debug|logging|snmp|ntp|aaa)\b',
    ]
    
    def __init__(
        self, 
        *args, 
        keyword_weight: float = 0.3,
        **kwargs
    ):
        """
        Args:
            keyword_weight: 키워드 매칭 가중치 (0.0 ~ 1.0)
        """
        super().__init__(*args, **kwargs)
        self.keyword_weight = keyword_weight
        self.compiled_patterns = [
            re.compile(p, re.IGNORECASE) 
            for p in self.CISCO_KEYWORD_PATTERNS
        ]
    
    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> RAGResponse:
        """
        하이브리드 검색 쿼리
        """
        # 1. 벡터 검색 (더 많이 가져옴)
        vector_results = self.vector_store.search(
            query=question,
            k=self.top_k * 2,
            filter_metadata=filter_metadata
        )
        
        # 2. 키워드 추출
        keywords = self._extract_cisco_keywords(question)
        logger.debug(f"Extracted keywords: {keywords}")
        
        # 3. 점수 재조정
        reranked_results = self._rerank_with_keywords(
            vector_results, 
            keywords
        )
        
        # 4. 상위 k개 선택
        top_results = reranked_results[:self.top_k]
        
        # 5. 필터링
        relevant_docs = [
            doc for doc in top_results 
            if doc['score'] >= self.score_threshold
        ]
        
        if not relevant_docs:
            return RAGResponse(
                answer="관련 정보를 찾을 수 없습니다.",
                sources=[],
                query=question,
                confidence=0.0
            )
        
        # 6. 응답 생성
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
    
    def _extract_cisco_keywords(self, text: str) -> List[str]:
        """
        시스코 관련 키워드 추출
        
        Args:
            text: 입력 텍스트
            
        Returns:
            추출된 키워드 리스트
        """
        keywords = []
        
        for pattern in self.compiled_patterns:
            matches = pattern.findall(text)
            keywords.extend(matches)
        
        # 중복 제거 및 소문자 정규화
        unique_keywords = list(set(kw.lower() for kw in keywords))
        
        return unique_keywords
    
    def _rerank_with_keywords(
        self, 
        results: List[Dict],
        keywords: List[str]
    ) -> List[Dict]:
        """
        키워드 기반 재순위화
        
        Args:
            results: 검색 결과
            keywords: 추출된 키워드
            
        Returns:
            재순위화된 결과
        """
        if not keywords:
            return results
        
        for result in results:
            content = result['content'].lower()
            
            # 키워드 매칭 점수 계산
            matched_keywords = sum(
                1 for kw in keywords 
                if kw.lower() in content
            )
            
            keyword_score = matched_keywords / len(keywords)
            
            # 정확한 매칭 보너스
            exact_match_bonus = 0
            for kw in keywords:
                if f" {kw.lower()} " in f" {content} ":
                    exact_match_bonus += 0.1
            
            # 점수 조합
            original_score = result['score']
            combined_score = (
                original_score * (1 - self.keyword_weight) +
                (keyword_score + exact_match_bonus) * self.keyword_weight
            )
            
            result['score'] = min(combined_score, 1.0)
            result['keyword_matches'] = matched_keywords
        
        # 재정렬
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results


class ConversationalRAG(CiscoRAGChain):
    """
    대화형 RAG - 이전 대화 컨텍스트 유지
    
    특징:
    - 대화 히스토리 관리
    - 문맥 기반 질문 해석
    - 후속 질문 지원
    """
    
    CONVERSATIONAL_SYSTEM_PROMPT = """당신은 시스코 네트워크 장비 전문가입니다.
사용자와의 대화 맥락을 고려하여 답변합니다.

이전 대화 내용을 참고하되, 새로운 질문에 집중하여 답변하세요.
"이전에 말씀드린 것처럼" 등의 표현을 적절히 사용할 수 있습니다.
답변은 한국어로 작성하되, CLI 명령어는 원어 그대로 사용하세요."""

    CONTEXT_RESOLUTION_PROMPT = """이전 대화 맥락을 고려하여 현재 질문을 완전한 형태로 다시 작성하세요.

이전 대화:
{history}

현재 질문: {question}

완전한 질문 (대명사나 생략된 부분을 명시적으로 포함):"""

    def __init__(
        self, 
        *args, 
        max_history: int = 5,
        resolve_context: bool = True,
        **kwargs
    ):
        """
        Args:
            max_history: 유지할 최대 대화 턴 수
            resolve_context: 문맥 기반 질문 재작성 여부
        """
        super().__init__(*args, **kwargs)
        self.conversation_history: List[Dict] = []
        self.max_history = max_history
        self.resolve_context = resolve_context
    
    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> RAGResponse:
        """
        대화형 쿼리
        """
        # 1. 문맥 기반 질문 재작성 (선택적)
        resolved_question = question
        if self.resolve_context and self.conversation_history:
            resolved_question = self._resolve_question_context(question)
            logger.debug(f"Resolved question: {resolved_question}")
        
        # 2. 문서 검색
        search_results = self.vector_store.search(
            query=resolved_question,
            k=self.top_k,
            filter_metadata=filter_metadata
        )
        
        relevant_docs = [
            doc for doc in search_results 
            if doc['score'] >= self.score_threshold
        ]
        
        # 3. 대화 히스토리 포함한 컨텍스트 구성
        history_context = self._build_history_context()
        doc_context = self._build_context(relevant_docs) if relevant_docs else "관련 문서 없음"
        
        prompt = f"""### 이전 대화:
{history_context}

### 참고 문서:
{doc_context}

### 현재 질문:
{question}

### 답변:"""
        
        # 4. 응답 생성
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.CONVERSATIONAL_SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        )
        
        # 5. 대화 히스토리 업데이트
        self._update_history(question, answer)
        
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs if include_sources else [],
            query=question,
            confidence=confidence
        )
    
    def _resolve_question_context(self, question: str) -> str:
        """
        이전 대화 맥락을 고려하여 질문 재작성
        
        Args:
            question: 현재 질문
            
        Returns:
            문맥이 해결된 완전한 질문
        """
        # 대명사나 생략이 있는지 간단히 체크
        context_indicators = ['그것', '이것', '그', '이', '저', '위', '아까', '방금', '그러면']
        has_context_reference = any(ind in question for ind in context_indicators)
        
        # 질문이 너무 짧은 경우도 문맥 해결 필요
        if not has_context_reference and len(question) > 20:
            return question
        
        history_text = self._build_history_context()
        
        prompt = self.CONTEXT_RESOLUTION_PROMPT.format(
            history=history_text,
            question=question
        )
        
        try:
            resolved = self.llm_service.generate(
                prompt=prompt,
                max_tokens=200,
                temperature=0.0
            )
            return resolved.strip()
        except Exception as e:
            logger.warning(f"Context resolution failed: {e}")
            return question
    
    def _build_history_context(self) -> str:
        """
        대화 히스토리 컨텍스트 구성
        
        Returns:
            포맷팅된 히스토리 문자열
        """
        if not self.conversation_history:
            return "이전 대화 없음"
        
        history_parts = []
        for turn in self.conversation_history[-self.max_history:]:
            history_parts.append(f"사용자: {turn['question']}")
            # 답변은 요약
            answer_summary = turn['answer'][:200]
            if len(turn['answer']) > 200:
                answer_summary += "..."
            history_parts.append(f"어시스턴트: {answer_summary}")
        
        return "\n".join(history_parts)
    
    def _update_history(self, question: str, answer: str):
        """
        대화 히스토리 업데이트
        
        Args:
            question: 질문
            answer: 답변
        """
        self.conversation_history.append({
            'question': question,
            'answer': answer
        })
        
        # 최대 길이 유지
        if len(self.conversation_history) > self.max_history * 2:
            self.conversation_history = self.conversation_history[-self.max_history:]
    
    def clear_history(self):
        """대화 히스토리 초기화"""
        self.conversation_history = []
        logger.info("Conversation history cleared")
    
    def get_history(self) -> List[Dict]:
        """대화 히스토리 반환"""
        return self.conversation_history.copy()


class StepByStepRAG(CiscoRAGChain):
    """
    단계별 절차 생성 특화 RAG
    
    설정 가이드, 트러블슈팅 등 절차적 답변에 적합
    """
    
    STEP_SYSTEM_PROMPT = """당신은 시스코 네트워크 장비 전문가입니다.
사용자의 요청에 대해 명확한 단계별 절차를 제공합니다.

답변 형식:
1. 사전 요구사항이나 주의사항을 먼저 안내
2. 각 단계를 번호로 구분 (1단계, 2단계...)
3. 각 단계에 필요한 CLI 명령어를 코드 블록으로 포함
4. 각 명령어에 대한 간단한 설명 추가
5. 검증 방법이나 예상 결과 제시
6. 문제 발생 시 확인할 사항 안내

명령어는 정확한 구문을 사용하고, 복잡한 설정은 부분별로 나누어 설명하세요.
답변은 한국어로 작성하되, CLI 명령어는 원어 그대로 사용하세요."""

    PROCEDURE_DETECTION_KEYWORDS = [
        '방법', '절차', '단계', '하는법', '설정', '구성',
        'how to', 'configure', 'setup', 'enable', 'create'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> RAGResponse:
        """
        단계별 절차 생성 쿼리
        """
        # 1. 질문을 절차 요청으로 변환
        procedure_question = self._convert_to_procedure_question(question)
        
        # 2. 문서 검색
        search_results = self.vector_store.search(
            query=procedure_question,
            k=self.top_k,
            filter_metadata=filter_metadata
        )
        
        relevant_docs = [
            doc for doc in search_results 
            if doc['score'] >= self.score_threshold
        ]
        
        # 3. CLI 명령어 문서 우선순위 높이기
        relevant_docs = self._prioritize_cli_docs(relevant_docs)
        
        context = self._build_context(relevant_docs) if relevant_docs else ""
        
        # 4. 절차 요청 프롬프트
        prompt = f"""### 참고 문서:
{context}

### 요청:
{question}

위 문서를 참고하여 단계별 절차를 작성해주세요.
각 단계에 필요한 명령어와 설명을 포함하세요.

### 단계별 절차:"""
        
        # 5. 응답 생성
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.STEP_SYSTEM_PROMPT,
            max_tokens=1500,
            temperature=0.1
        )
        
        # 6. 응답 후처리
        answer = self._format_step_response(answer)
        
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs if include_sources else [],
            query=question,
            confidence=confidence
        )
    
    def _convert_to_procedure_question(self, question: str) -> str:
        """
        질문을 절차 검색에 적합하게 변환
        
        Args:
            question: 원본 질문
            
        Returns:
            변환된 질문
        """
        # 절차 관련 키워드 확인
        has_procedure_keyword = any(
            kw in question.lower() 
            for kw in self.PROCEDURE_DETECTION_KEYWORDS
        )
        
        if not has_procedure_keyword:
            return f"{question} 설정 방법 절차 명령어"
        
        return question
    
    def _prioritize_cli_docs(self, docs: List[Dict]) -> List[Dict]:
        """
        CLI 명령어 문서 우선순위 높이기
        
        Args:
            docs: 문서 리스트
            
        Returns:
            재정렬된 문서 리스트
        """
        cli_docs = []
        other_docs = []
        
        for doc in docs:
            if doc.get('metadata', {}).get('chunk_type') == 'cli_command':
                cli_docs.append(doc)
            else:
                other_docs.append(doc)
        
        # CLI 문서를 앞에, 나머지는 뒤에
        return cli_docs + other_docs
    
    def _format_step_response(self, answer: str) -> str:
        """
        단계별 응답 포맷팅
        
        Args:
            answer: 원본 응답
            
        Returns:
            포맷팅된 응답
        """
        # 기본 포맷팅은 LLM이 처리하므로 최소한의 정리만
        
        # 빈 줄 정리
        lines = answer.split('\n')
        cleaned_lines = []
        prev_empty = False
        
        for line in lines:
            is_empty = not line.strip()
            if is_empty and prev_empty:
                continue
            cleaned_lines.append(line)
            prev_empty = is_empty
        
        return '\n'.join(cleaned_lines)


class TroubleshootingRAG(CiscoRAGChain):
    """
    트러블슈팅 특화 RAG
    
    특징:
    - 증상 기반 검색
    - 진단 명령어 우선 제공
    - 해결책 단계별 안내
    """
    
    TROUBLESHOOTING_SYSTEM_PROMPT = """당신은 시스코 네트워크 장비 트러블슈팅 전문가입니다.

문제 해결 답변 형식:
1. **문제 분석**: 증상에 대한 가능한 원인 설명
2. **진단 명령어**: 문제 확인을 위한 show/debug 명령어
3. **예상 출력**: 각 명령어의 정상/비정상 출력 예시
4. **해결 방법**: 원인별 해결 절차
5. **확인 방법**: 문제 해결 여부 확인 방법

진단 명령어를 먼저 제시하여 문제 원인을 파악할 수 있게 하세요.
답변은 한국어로 작성하되, CLI 명령어는 원어 그대로 사용하세요."""

    DIAGNOSTIC_COMMANDS = {
        'interface': ['show interface', 'show interface status', 'show running-config interface'],
        'vlan': ['show vlan brief', 'show vlan', 'show interfaces trunk'],
        'routing': ['show ip route', 'show ip protocols', 'show ip ospf neighbor'],
        'spanning-tree': ['show spanning-tree', 'show spanning-tree summary'],
        'connectivity': ['ping', 'traceroute', 'show arp', 'show mac address-table'],
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> RAGResponse:
        """
        트러블슈팅 쿼리
        """
        # 1. 문제 유형 감지
        problem_type = self._detect_problem_type(question)
        
        # 2. 관련 진단 명령어 추가
        diagnostic_cmds = self.DIAGNOSTIC_COMMANDS.get(problem_type, [])
        
        # 3. 문서 검색 (증상 + 진단 명령어 포함)
        enhanced_query = f"{question} 문제 해결 진단 {' '.join(diagnostic_cmds)}"
        
        search_results = self.vector_store.search(
            query=enhanced_query,
            k=self.top_k,
            filter_metadata=filter_metadata
        )
        
        relevant_docs = [
            doc for doc in search_results 
            if doc['score'] >= self.score_threshold
        ]
        
        context = self._build_context(relevant_docs) if relevant_docs else ""
        
        # 4. 트러블슈팅 프롬프트
        prompt = f"""### 참고 문서:
{context}

### 관련 진단 명령어:
{', '.join(diagnostic_cmds) if diagnostic_cmds else '일반 진단 명령어 사용'}

### 문제 상황:
{question}

### 트러블슈팅 가이드:"""
        
        # 5. 응답 생성
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.TROUBLESHOOTING_SYSTEM_PROMPT,
            max_tokens=1500,
            temperature=0.1
        )
        
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs if include_sources else [],
            query=question,
            confidence=confidence
        )
    
    def _detect_problem_type(self, question: str) -> str:
        """
        문제 유형 감지
        
        Args:
            question: 질문
            
        Returns:
            문제 유형 문자열
        """
        question_lower = question.lower()
        
        type_keywords = {
            'interface': ['인터페이스', 'interface', '포트', 'port', 'link', '연결'],
            'vlan': ['vlan', '브이랜', '가상랜'],
            'routing': ['라우팅', 'routing', 'route', '경로', 'ospf', 'eigrp', 'bgp'],
            'spanning-tree': ['stp', 'spanning', '스패닝', '루프', 'loop'],
            'connectivity': ['통신', '핑', 'ping', '연결', '접속', '안됨', '안됨'],
        }
        
        for problem_type, keywords in type_keywords.items():
            if any(kw in question_lower for kw in keywords):
                return problem_type
        
        return 'connectivity'  # 기본값


class SummaryRAG(CiscoRAGChain):
    """
    요약 기능 특화 RAG
    
    긴 문서나 여러 문서를 요약하여 제공
    """
    
    SUMMARY_SYSTEM_PROMPT = """당신은 시스코 네트워크 기술 문서 요약 전문가입니다.

요약 지침:
1. 핵심 개념과 중요 정보를 중심으로 요약
2. CLI 명령어가 있으면 주요 명령어 포함
3. 주의사항이나 제한사항 포함
4. 관련 참조 정보 언급

간결하고 명확하게 요약하되, 중요한 기술적 세부사항은 유지하세요."""

    def __init__(self, *args, summary_max_length: int = 500, **kwargs):
        super().__init__(*args, **kwargs)
        self.summary_max_length = summary_max_length
    
    def summarize_topic(
        self,
        topic: str,
        filter_metadata: Optional[Dict] = None
    ) -> RAGResponse:
        """
        특정 주제에 대한 문서 요약
        
        Args:
            topic: 요약할 주제
            filter_metadata: 메타데이터 필터
            
        Returns:
            RAGResponse 객체
        """
        # 관련 문서 검색 (더 많이)
        search_results = self.vector_store.search(
            query=topic,
            k=self.top_k * 2,
            filter_metadata=filter_metadata
        )
        
        relevant_docs = [
            doc for doc in search_results 
            if doc['score'] >= self.score_threshold
        ]
        
        if not relevant_docs:
            return RAGResponse(
                answer="해당 주제에 대한 문서를 찾을 수 없습니다.",
                sources=[],
                query=topic,
                confidence=0.0
            )
        
        # 문서 내용 결합
        combined_content = "\n\n---\n\n".join([
            doc['content'] for doc in relevant_docs
        ])
        
        prompt = f"""다음 문서들을 {self.summary_max_length}자 이내로 요약하세요.

### 주제:
{topic}

### 문서 내용:
{combined_content[:3000]}  # 토큰 제한

### 요약:"""
        
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.SUMMARY_SYSTEM_PROMPT,
            max_tokens=800,
            temperature=0.1
        )
        
        confidence = self._calculate_confidence(relevant_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=relevant_docs,
            query=topic,
            confidence=confidence
        )


class ComparisonRAG(CiscoRAGChain):
    """
    비교 분석 특화 RAG
    
    두 가지 이상의 기술/설정 비교
    """
    
    COMPARISON_SYSTEM_PROMPT = """당신은 시스코 네트워크 기술 비교 분석 전문가입니다.

비교 답변 형식:
1. 각 항목에 대한 간단한 설명
2. 주요 차이점 (표 형식 권장)
3. 각각의 장단점
4. 사용 시나리오 및 권장 사항

객관적이고 균형 잡힌 비교를 제공하세요.
답변은 한국어로 작성하되, 기술 용어는 원어 그대로 사용하세요."""

    def compare(
        self,
        item1: str,
        item2: str,
        aspect: Optional[str] = None
    ) -> RAGResponse:
        """
        두 항목 비교
        
        Args:
            item1: 첫 번째 비교 항목
            item2: 두 번째 비교 항목
            aspect: 비교 관점 (선택)
            
        Returns:
            RAGResponse 객체
        """
        # 각 항목에 대한 문서 검색
        results1 = self.vector_store.search(query=item1, k=3)
        results2 = self.vector_store.search(query=item2, k=3)
        
        all_docs = results1 + results2
        
        # 컨텍스트 구성
        context1 = self._build_context(results1[:2]) if results1 else "문서 없음"
        context2 = self._build_context(results2[:2]) if results2 else "문서 없음"
        
        aspect_text = f" ({aspect} 관점에서)" if aspect else ""
        
        prompt = f"""다음 문서들을 참고하여 {item1}와(과) {item2}를 비교 분석하세요{aspect_text}.

### {item1} 관련 문서:
{context1}

### {item2} 관련 문서:
{context2}

### 비교 분석:"""
        
        answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.COMPARISON_SYSTEM_PROMPT,
            max_tokens=1200,
            temperature=0.1
        )
        
        confidence = self._calculate_confidence(all_docs, answer)
        
        return RAGResponse(
            answer=answer,
            sources=all_docs,
            query=f"{item1} vs {item2}",
            confidence=confidence
        )