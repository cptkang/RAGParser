# src/rag/multilingual_rag.py

from typing import List, Dict, Optional, Generator
import logging

from .rag_chain import CiscoRAGChain, RAGResponse
from ..translation.translator import BaseTranslator, create_translator
from ..vectorstore.chroma_store import CiscoVectorStore
from ..llm.llama_service import BaseLlamaService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MultilingualRAGChain(CiscoRAGChain):
    """
    다국어 지원 RAG 체인

    특징:
    - 한국어 질문 → 영어로 번역 → RAG 검색
    - 영어 답변 → 한국어로 번역
    - 기술 용어/CLI 명령어는 원어 유지

    사용 사례:
    시스코 매뉴얼이 영문으로 작성되어 있어도 한국어로 질의응답 가능
    """

    # 다국어 시스템 프롬프트
    MULTILINGUAL_SYSTEM_PROMPT = """You are a Cisco network equipment expert.
Provide accurate and practical answers based on the provided manual context.

Guidelines:
1. Answer based solely on the provided context information.
2. Use correct CLI command syntax when including commands.
3. Clearly separate and explain step-by-step procedures when needed.
4. If information is not in the context, state "The requested information cannot be found in the provided documents."
5. Always include relevant warnings or cautions.

Keep technical terms and CLI commands in their original form."""

    def __init__(
        self,
        vector_store: CiscoVectorStore,
        llm_service: Optional[BaseLlamaService] = None,
        translator: Optional[BaseTranslator] = None,
        translator_type: str = "google",
        source_lang: str = "ko",
        manual_lang: str = "en",
        top_k: int = 5,
        score_threshold: float = 0.5,
        enable_translation: bool = True
    ):
        """
        Args:
            vector_store: 벡터 스토어 인스턴스
            llm_service: LLM 서비스 인스턴스
            translator: 번역기 인스턴스 (없으면 자동 생성)
            translator_type: 번역기 타입 ('google', 'deepl', 'llm')
            source_lang: 사용자 입력 언어 (기본: 한국어)
            manual_lang: 매뉴얼 언어 (기본: 영어)
            top_k: 검색할 문서 수
            score_threshold: 최소 유사도 점수
            enable_translation: 번역 활성화 여부
        """
        super().__init__(
            vector_store=vector_store,
            llm_service=llm_service,
            top_k=top_k,
            score_threshold=score_threshold
        )

        self.source_lang = source_lang
        self.manual_lang = manual_lang
        self.enable_translation = enable_translation

        # 번역기 초기화
        if enable_translation:
            if translator is None:
                try:
                    if translator_type == "llm":
                        translator = create_translator(
                            translator_type="llm",
                            llm_service=self.llm_service
                        )
                    else:
                        translator = create_translator(translator_type=translator_type)
                    logger.info(f"Translator initialized: {translator_type}")
                except Exception as e:
                    logger.warning(f"Failed to initialize translator: {e}. Translation disabled.")
                    self.enable_translation = False

            self.translator = translator
        else:
            self.translator = None

        logger.info(f"MultilingualRAGChain initialized (translation: {self.enable_translation})")

    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True,
        return_original_response: bool = False
    ) -> RAGResponse:
        """
        다국어 RAG 쿼리 실행

        Args:
            question: 사용자 질문 (한국어)
            filter_metadata: 메타데이터 필터
            include_sources: 소스 포함 여부
            return_original_response: 원본 영어 응답도 반환할지 여부

        Returns:
            RAGResponse 객체 (한국어 답변)
        """
        # 번역이 비활성화되어 있으면 기본 동작
        if not self.enable_translation:
            return super().query(question, filter_metadata, include_sources)

        # 1. 언어 감지
        detected_lang = self.translator.detect_language(question)
        logger.debug(f"Detected language: {detected_lang}")

        # 2. 질문 번역 (한국어 → 영어)
        translated_question = question
        if detected_lang != self.manual_lang:
            try:
                translated_question = self.translator.translate(
                    text=question,
                    source_lang=detected_lang,
                    target_lang=self.manual_lang
                )
                logger.info(f"Question translated: {question[:50]}... → {translated_question[:50]}...")
            except Exception as e:
                logger.error(f"Question translation failed: {e}")
                # 번역 실패 시 원본 사용

        # 3. 영어로 문서 검색
        search_results = self.vector_store.search(
            query=translated_question,
            k=self.top_k,
            filter_metadata=filter_metadata
        )

        # 4. 점수 기준 필터링
        relevant_docs = [
            doc for doc in search_results
            if doc['score'] >= self.score_threshold
        ]

        if not relevant_docs:
            no_result_message = "제공된 문서에서 관련 정보를 찾을 수 없습니다. 다른 키워드로 검색해 주세요."
            return RAGResponse(
                answer=no_result_message,
                sources=[],
                query=question,
                confidence=0.0
            )

        # 5. 영어 컨텍스트 구성
        context = self._build_context(relevant_docs)

        # 6. 영어 프롬프트 생성
        prompt = f"""Reference the following context to answer the question.

### Context:
{context}

### Question:
{translated_question}

### Answer:"""

        # 7. 영어로 LLM 응답 생성
        english_answer = self.llm_service.generate(
            prompt=prompt,
            system_prompt=self.MULTILINGUAL_SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        )

        logger.debug(f"English answer: {english_answer[:100]}...")

        # 8. 답변 번역 (영어 → 한국어)
        korean_answer = english_answer
        try:
            korean_answer = self._translate_answer(english_answer, detected_lang)
            logger.info("Answer translated to Korean")
        except Exception as e:
            logger.error(f"Answer translation failed: {e}")
            # 번역 실패 시 영어 답변 사용

        # 9. 신뢰도 계산
        confidence = self._calculate_confidence(relevant_docs, english_answer)

        response = RAGResponse(
            answer=korean_answer,
            sources=relevant_docs if include_sources else [],
            query=question,
            confidence=confidence
        )

        # 원본 영어 응답 저장 (디버깅용)
        if return_original_response:
            response.original_answer = english_answer
            response.translated_question = translated_question

        return response

    def query_stream(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None
    ) -> Generator[str, None, None]:
        """
        스트리밍 다국어 RAG 쿼리

        Args:
            question: 사용자 질문 (한국어)
            filter_metadata: 메타데이터 필터

        Yields:
            응답 토큰 (한국어)
        """
        # 번역이 비활성화되어 있으면 기본 동작
        if not self.enable_translation:
            yield from super().query_stream(question, filter_metadata)
            return

        # 1. 언어 감지
        detected_lang = self.translator.detect_language(question)

        # 2. 질문 번역
        translated_question = question
        if detected_lang != self.manual_lang:
            try:
                translated_question = self.translator.translate(
                    text=question,
                    source_lang=detected_lang,
                    target_lang=self.manual_lang
                )
            except Exception as e:
                logger.error(f"Question translation failed: {e}")

        # 3. 문서 검색
        search_results = self.vector_store.search(
            query=translated_question,
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

        # 4. 컨텍스트 및 프롬프트 구성
        context = self._build_context(relevant_docs)
        prompt = f"""Reference the following context to answer the question.

### Context:
{context}

### Question:
{translated_question}

### Answer:"""

        # 5. 영어 스트리밍 응답 수집
        english_answer_parts = []
        for token in self.llm_service.generate_stream(
            prompt=prompt,
            system_prompt=self.MULTILINGUAL_SYSTEM_PROMPT,
            max_tokens=1024,
            temperature=0.1
        ):
            english_answer_parts.append(token)

        # 6. 전체 답변 번역
        english_answer = "".join(english_answer_parts)
        try:
            korean_answer = self._translate_answer(english_answer, detected_lang)
            yield korean_answer
        except Exception as e:
            logger.error(f"Answer translation failed: {e}")
            yield english_answer

    def _translate_answer(self, answer: str, target_lang: str) -> str:
        """
        답변 번역 (기술 용어와 CLI 명령어 보존)

        Args:
            answer: 영어 답변
            target_lang: 타겟 언어

        Returns:
            번역된 답변
        """
        import re

        # CLI 명령어 블록 보호
        code_blocks = []
        code_block_pattern = r'```[\s\S]*?```'

        def replace_code_block(match):
            code_blocks.append(match.group(0))
            return f"__CODE_BLOCK_{len(code_blocks) - 1}__"

        # 코드 블록을 임시 태그로 치환
        protected_answer = re.sub(code_block_pattern, replace_code_block, answer)

        # 인라인 코드 보호
        inline_codes = []
        inline_code_pattern = r'`[^`]+`'

        def replace_inline_code(match):
            inline_codes.append(match.group(0))
            return f"__INLINE_CODE_{len(inline_codes) - 1}__"

        protected_answer = re.sub(inline_code_pattern, replace_inline_code, protected_answer)

        # 번역 실행
        try:
            translated = self.translator.translate(
                text=protected_answer,
                source_lang=self.manual_lang,
                target_lang=target_lang
            )
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return answer

        # 코드 블록 복원
        for i, code_block in enumerate(code_blocks):
            translated = translated.replace(f"__CODE_BLOCK_{i}__", code_block)

        # 인라인 코드 복원
        for i, inline_code in enumerate(inline_codes):
            translated = translated.replace(f"__INLINE_CODE_{i}__", inline_code)

        return translated

    def query_cli_command(
        self,
        command_description: str
    ) -> RAGResponse:
        """
        CLI 명령어 전용 검색 (다국어 지원)

        Args:
            command_description: 명령어 설명 (한국어)

        Returns:
            RAGResponse 객체
        """
        return self.query(
            question=command_description,
            filter_metadata={"chunk_type": "cli_command"}
        )

    def set_translation_enabled(self, enabled: bool):
        """
        번역 기능 활성화/비활성화

        Args:
            enabled: 활성화 여부
        """
        self.enable_translation = enabled
        logger.info(f"Translation {'enabled' if enabled else 'disabled'}")


class BilingualRAGChain(MultilingualRAGChain):
    """
    이중 언어 RAG 체인

    특징:
    - 한국어와 영어 답변을 모두 제공
    - 비교 학습이나 검증에 유용
    """

    def query(
        self,
        question: str,
        filter_metadata: Optional[Dict] = None,
        include_sources: bool = True
    ) -> Dict[str, RAGResponse]:
        """
        이중 언어 RAG 쿼리 실행

        Args:
            question: 사용자 질문
            filter_metadata: 메타데이터 필터
            include_sources: 소스 포함 여부

        Returns:
            {'korean': RAGResponse, 'english': RAGResponse} 딕셔너리
        """
        # 1. 영어 답변 생성
        english_response = super().query(
            question=question,
            filter_metadata=filter_metadata,
            include_sources=include_sources,
            return_original_response=True
        )

        # 2. 영어 답변 추출
        original_answer = getattr(english_response, 'original_answer', None)

        if original_answer is None:
            # 번역이 비활성화된 경우
            return {
                'korean': english_response,
                'english': english_response
            }

        # 3. 영어 RAGResponse 생성
        english_response_obj = RAGResponse(
            answer=original_answer,
            sources=english_response.sources,
            query=getattr(english_response, 'translated_question', question),
            confidence=english_response.confidence
        )

        return {
            'korean': english_response,
            'english': english_response_obj
        }


def create_multilingual_rag(
    vector_store: CiscoVectorStore,
    llm_service: Optional[BaseLlamaService] = None,
    translator_type: str = "google",
    bilingual: bool = False,
    **kwargs
) -> CiscoRAGChain:
    """
    다국어 RAG 체인 팩토리 함수

    Args:
        vector_store: 벡터 스토어
        llm_service: LLM 서비스
        translator_type: 번역기 타입 ('google', 'deepl', 'llm')
        bilingual: 이중 언어 모드 사용 여부
        **kwargs: 추가 인자

    Returns:
        MultilingualRAGChain 또는 BilingualRAGChain 인스턴스
    """
    if bilingual:
        return BilingualRAGChain(
            vector_store=vector_store,
            llm_service=llm_service,
            translator_type=translator_type,
            **kwargs
        )
    else:
        return MultilingualRAGChain(
            vector_store=vector_store,
            llm_service=llm_service,
            translator_type=translator_type,
            **kwargs
        )
