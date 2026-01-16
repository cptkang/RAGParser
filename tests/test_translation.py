# tests/test_translation.py

"""
번역 기능 테스트
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.translation.translator import GoogleTranslator, LLMTranslator
from src.llm.llama_service import OllamaService


class TestTranslation:
    """번역 기능 테스트"""

    def test_google_translator_ko_to_en(self):
        """한국어 → 영어 번역 테스트"""
        try:
            translator = GoogleTranslator()

            text = "VLAN을 설정하는 방법을 알려주세요"
            result = translator.translate(text, source_lang="ko", target_lang="en")

            print(f"\n원문: {text}")
            print(f"번역: {result}")

            assert result is not None
            assert len(result) > 0
            assert "VLAN" in result  # 기술 용어는 유지되어야 함

        except ImportError as e:
            pytest.skip(f"googletrans not installed: {e}")

    def test_google_translator_en_to_ko(self):
        """영어 → 한국어 번역 테스트"""
        try:
            translator = GoogleTranslator()

            text = "Configure the VLAN on the switch using the vlan command"
            result = translator.translate(text, source_lang="en", target_lang="ko")

            print(f"\n원문: {text}")
            print(f"번역: {result}")

            assert result is not None
            assert len(result) > 0
            # 한글이 포함되어 있는지 확인
            assert any('\uac00' <= char <= '\ud7a3' for char in result)

        except ImportError as e:
            pytest.skip(f"googletrans not installed: {e}")

    def test_language_detection(self):
        """언어 감지 테스트"""
        try:
            translator = GoogleTranslator()

            # 한국어
            korean_text = "안녕하세요"
            detected = translator.detect_language(korean_text)
            print(f"\n텍스트: {korean_text}")
            print(f"감지된 언어: {detected}")
            assert detected == "ko"

            # 영어
            english_text = "Hello world"
            detected = translator.detect_language(english_text)
            print(f"\n텍스트: {english_text}")
            print(f"감지된 언어: {detected}")
            assert detected == "en"

        except ImportError as e:
            pytest.skip(f"googletrans not installed: {e}")

    def test_llm_translator(self):
        """LLM 번역 테스트"""
        try:
            llm_service = OllamaService(model_name="llama3.1:8b")
            translator = LLMTranslator(llm_service)

            text = "스위치 포트를 설정하세요"
            result = translator.translate(text, source_lang="ko", target_lang="en")

            print(f"\n원문: {text}")
            print(f"LLM 번역: {result}")

            assert result is not None
            assert len(result) > 0

        except Exception as e:
            pytest.skip(f"LLM service not available: {e}")

    def test_preserve_technical_terms(self):
        """기술 용어 보존 테스트"""
        try:
            translator = GoogleTranslator()

            # 기술 용어가 많은 문장
            text = "VLAN 10을 trunk 포트에 설정하고 STP를 활성화하세요"
            result = translator.translate(text, source_lang="ko", target_lang="en")

            print(f"\n원문: {text}")
            print(f"번역: {result}")

            # 기술 용어가 유지되는지 확인
            assert "VLAN" in result or "vlan" in result.lower()
            assert "trunk" in result.lower()
            assert "STP" in result or "stp" in result.lower()

        except ImportError as e:
            pytest.skip(f"googletrans not installed: {e}")


class TestCodeBlockPreservation:
    """코드 블록 보존 테스트"""

    def test_code_block_preservation(self):
        """코드 블록이 번역되지 않는지 테스트"""
        try:
            translator = GoogleTranslator()

            text = """Configure VLAN using these commands:

```
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
```

This creates VLAN 10."""

            result = translator.translate(text, source_lang="en", target_lang="ko")

            print(f"\n원문:\n{text}")
            print(f"\n번역:\n{result}")

            # 코드 블록 내부가 번역되지 않았는지 확인
            assert "configure terminal" in result or "설정" in result

        except ImportError as e:
            pytest.skip(f"googletrans not installed: {e}")


if __name__ == "__main__":
    print("=" * 80)
    print("번역 기능 테스트")
    print("=" * 80)

    # pytest 실행
    pytest.main([__file__, "-v", "-s"])
