# src/translation/translator.py

from typing import Optional
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseTranslator(ABC):
    """번역 서비스 기본 클래스"""

    @abstractmethod
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """텍스트 번역

        Args:
            text: 번역할 텍스트
            source_lang: 소스 언어 코드
            target_lang: 타겟 언어 코드

        Returns:
            번역된 텍스트
        """
        pass

    def detect_language(self, text: str) -> str:
        """언어 감지

        Args:
            text: 감지할 텍스트

        Returns:
            언어 코드
        """
        pass


class DeepLTranslator(BaseTranslator):
    """
    DeepL API를 사용한 번역 서비스

    고품질 번역 제공 (무료 API: 월 500,000자)
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Args:
            api_key: DeepL API 키 (없으면 환경변수에서 읽음)
        """
        import os

        self.api_key = api_key or os.getenv('DEEPL_API_KEY')
        if not self.api_key:
            raise ValueError("DeepL API key not provided. Set DEEPL_API_KEY environment variable.")

        try:
            import deepl
            self.translator = deepl.Translator(self.api_key)
            logger.info("DeepL translator initialized")
        except ImportError:
            raise ImportError("deepl library not installed. Run: pip install deepl")

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        텍스트 번역

        Args:
            text: 번역할 텍스트
            source_lang: 소스 언어 ('ko', 'en', 'ja' 등)
            target_lang: 타겟 언어

        Returns:
            번역된 텍스트
        """
        try:
            # DeepL 언어 코드 변환
            target_lang_code = self._convert_lang_code(target_lang)

            result = self.translator.translate_text(
                text,
                source_lang=source_lang.upper() if source_lang else None,
                target_lang=target_lang_code
            )

            return result.text

        except Exception as e:
            logger.error(f"Translation error: {e}")
            return text

    def _convert_lang_code(self, lang_code: str) -> str:
        """
        DeepL API 언어 코드 변환

        Args:
            lang_code: 언어 코드

        Returns:
            DeepL API 언어 코드
        """
        # 한국어는 KO, 영어는 EN-US 등
        mapping = {
            'ko': 'KO',
            'en': 'EN-US',
            'ja': 'JA',
            'zh': 'ZH'
        }

        return mapping.get(lang_code.lower(), lang_code.upper())

    def detect_language(self, text: str) -> str:
        """
        언어 감지 (간단한 휴리스틱)

        Args:
            text: 감지할 텍스트

        Returns:
            언어 코드
        """
        # 한글이 포함되어 있으면 한국어
        if any('\uac00' <= char <= '\ud7a3' for char in text):
            return 'ko'

        # 일본어 문자
        if any('\u3040' <= char <= '\u309f' or '\u30a0' <= char <= '\u30ff' for char in text):
            return 'ja'

        # 중국어 문자
        if any('\u4e00' <= char <= '\u9fff' for char in text):
            return 'zh'

        # 기본값은 영어
        return 'en'


class GoogleTranslator(BaseTranslator):
    """
    Google Translate API를 사용한 번역 서비스

    무료 라이브러리 사용 (googletrans)
    """

    def __init__(self):
        """Google Translator 초기화"""
        try:
            from googletrans import Translator
            self.translator = Translator()
            logger.info("Google translator initialized")
        except ImportError:
            raise ImportError("googletrans library not installed. Run: pip install googletrans==4.0.0rc1")

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        텍스트 번역

        Args:
            text: 번역할 텍스트
            source_lang: 소스 언어 ('ko', 'en', 'ja' 등)
            target_lang: 타겟 언어

        Returns:
            번역된 텍스트
        """
        try:
            result = self.translator.translate(
                text,
                src=source_lang if source_lang else 'auto',
                dest=target_lang
            )
            return result.text

        except Exception as e:
            logger.error(f"Translation error: {e}")
            return text

    def detect_language(self, text: str) -> str:
        """
        언어 감지

        Args:
            text: 감지할 텍스트

        Returns:
            언어 코드
        """
        try:
            result = self.translator.detect(text)
            return result.lang
        except Exception as e:
            logger.error(f"Language detection error: {e}")
            # 폴백: 간단한 휴리스틱
            if any('\uac00' <= char <= '\ud7a3' for char in text):
                return 'ko'
            return 'en'


class LLMTranslator(BaseTranslator):
    """
    LLM을 사용한 번역 서비스

    외부 API 없이 로컬 LLM으로 번역
    """

    def __init__(self, llm_service):
        """
        Args:
            llm_service: BaseLlamaService 인스턴스
        """
        self.llm_service = llm_service
        logger.info("LLM translator initialized")

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        텍스트 번역

        Args:
            text: 번역할 텍스트
            source_lang: 소스 언어 ('ko', 'en', 'ja' 등)
            target_lang: 타겟 언어

        Returns:
            번역된 텍스트
        """
        lang_names = {
            'ko': '한국어',
            'en': '영어',
            'ja': '일본어',
            'zh': '중국어'
        }

        source_name = lang_names.get(source_lang, source_lang)
        target_name = lang_names.get(target_lang, target_lang)

        prompt = f"""다음 {source_name} 텍스트를 {target_name}로 번역하세요.
기술 용어, CLI 명령어, 설정 파라미터는 원어 그대로 유지하세요.
번역만 출력하고 다른 설명은 하지 마세요.

텍스트:
{text}

번역:"""

        try:
            translation = self.llm_service.generate(
                prompt=prompt,
                max_tokens=2000,
                temperature=0.1
            )

            return translation.strip()

        except Exception as e:
            logger.error(f"LLM translation error: {e}")
            return text

    def detect_language(self, text: str) -> str:
        """
        언어 감지 (간단한 휴리스틱)

        Args:
            text: 감지할 텍스트

        Returns:
            언어 코드
        """
        # 한글이 포함되어 있으면 한국어
        if any('\uac00' <= char <= '\ud7a3' for char in text):
            return 'ko'

        # 일본어 문자
        if any('\u3040' <= char <= '\u309f' or '\u30a0' <= char <= '\u30ff' for char in text):
            return 'ja'

        # 중국어 문자
        if any('\u4e00' <= char <= '\u9fff' for char in text):
            return 'zh'

        # 기본값은 영어
        return 'en'


def create_translator(
    translator_type: str = "google",
    api_key: Optional[str] = None,
    llm_service = None
) -> BaseTranslator:
    """
    번역기 팩토리 함수

    Args:
        translator_type: 번역기 타입 ('deepl', 'google', 'llm')
        api_key: API 키 (DeepL용)
        llm_service: LLM 서비스 (LLM 번역용)

    Returns:
        BaseTranslator 인스턴스
    """
    if translator_type == "deepl":
        return DeepLTranslator(api_key=api_key)
    elif translator_type == "google":
        return GoogleTranslator()
    elif translator_type == "llm":
        if llm_service is None:
            raise ValueError("llm_service is required for LLM translator")
        return LLMTranslator(llm_service=llm_service)
    else:
        raise ValueError(f"Unknown translator type: {translator_type}")
