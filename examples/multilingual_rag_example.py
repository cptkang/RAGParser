# examples/multilingual_rag_example.py

"""
다국어 RAG 체인 사용 예제

시스코 매뉴얼이 영문으로 작성되어 있어도 한국어로 질의응답
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.vectorstore.chroma_store import CiscoVectorStore
from src.llm.llama_service import OllamaService
from src.rag.multilingual_rag import create_multilingual_rag


def example_basic_translation():
    """기본 번역 예제"""
    print("=" * 80)
    print("예제 1: 기본 다국어 RAG")
    print("=" * 80)

    # 1. 벡터 스토어 초기화
    vector_store = CiscoVectorStore(
        collection_name="cisco_manuals",
        persist_directory="./data/chroma_db"
    )

    # 2. LLM 서비스 초기화
    llm_service = OllamaService(model_name="llama3.1:8b")

    # 3. 다국어 RAG 체인 생성
    rag = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="google",  # 또는 "deepl", "llm"
        enable_translation=True
    )

    # 4. 한국어로 질문
    question = "VLAN을 설정하는 방법을 알려주세요"

    print(f"\n질문 (한국어): {question}")
    print("\n처리 과정:")
    print("1. 한국어 질문 감지")
    print("2. 영어로 번역하여 영문 매뉴얼 검색")
    print("3. 영어 답변 생성")
    print("4. 한국어로 번역하여 반환")

    # 5. 쿼리 실행
    response = rag.query(question)

    print("\n" + "-" * 80)
    print(f"답변 (한국어):\n{response.answer}")
    print(f"\n신뢰도: {response.confidence:.2f}")

    if response.sources:
        print(f"\n참조 문서 수: {len(response.sources)}")
        print("\n상위 참조:")
        for i, source in enumerate(response.sources[:2], 1):
            print(f"\n{i}. 점수: {source['score']:.3f}")
            print(f"   내용: {source['content'][:100]}...")


def example_bilingual_output():
    """이중 언어 출력 예제"""
    print("\n" + "=" * 80)
    print("예제 2: 이중 언어 모드")
    print("=" * 80)

    vector_store = CiscoVectorStore(
        collection_name="cisco_manuals",
        persist_directory="./data/chroma_db"
    )

    llm_service = OllamaService(model_name="llama3.1:8b")

    # 이중 언어 모드로 생성
    rag = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="google",
        bilingual=True  # 한국어와 영어 답변 모두 제공
    )

    question = "스위치 포트를 trunk 모드로 설정하는 CLI 명령어는?"

    print(f"\n질문: {question}")

    # 이중 언어 응답
    responses = rag.query(question)

    print("\n" + "-" * 80)
    print("한국어 답변:")
    print(responses['korean'].answer)

    print("\n" + "-" * 80)
    print("영어 답변 (원문):")
    print(responses['english'].answer)


def example_translation_types():
    """다양한 번역기 사용 예제"""
    print("\n" + "=" * 80)
    print("예제 3: 다양한 번역기 비교")
    print("=" * 80)

    vector_store = CiscoVectorStore(
        collection_name="cisco_manuals",
        persist_directory="./data/chroma_db"
    )

    llm_service = OllamaService(model_name="llama3.1:8b")

    question = "인터페이스 상태를 확인하는 명령어는?"

    # 1. Google Translate 사용
    print("\n1. Google Translate 사용")
    print("-" * 40)
    rag_google = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="google"
    )
    response_google = rag_google.query(question)
    print(f"답변: {response_google.answer[:200]}...")

    # 2. LLM 번역 사용 (외부 API 불필요)
    print("\n2. LLM 번역 사용 (로컬)")
    print("-" * 40)
    rag_llm = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="llm"
    )
    response_llm = rag_llm.query(question)
    print(f"답변: {response_llm.answer[:200]}...")

    # 3. DeepL 사용 (API 키 필요)
    # print("\n3. DeepL 사용 (고품질)")
    # print("-" * 40)
    # try:
    #     rag_deepl = create_multilingual_rag(
    #         vector_store=vector_store,
    #         llm_service=llm_service,
    #         translator_type="deepl"
    #     )
    #     response_deepl = rag_deepl.query(question)
    #     print(f"답변: {response_deepl.answer[:200]}...")
    # except Exception as e:
    #     print(f"DeepL 사용 불가: {e}")


def example_streaming():
    """스트리밍 다국어 RAG 예제"""
    print("\n" + "=" * 80)
    print("예제 4: 스트리밍 응답")
    print("=" * 80)

    vector_store = CiscoVectorStore(
        collection_name="cisco_manuals",
        persist_directory="./data/chroma_db"
    )

    llm_service = OllamaService(model_name="llama3.1:8b")

    rag = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="google"
    )

    question = "OSPF 라우팅 프로토콜을 활성화하는 방법은?"

    print(f"\n질문: {question}")
    print("\n답변 (스트리밍):")
    print("-" * 80)

    # 스트리밍 응답 (주의: 번역은 전체 답변 생성 후 수행됨)
    for token in rag.query_stream(question):
        print(token, end='', flush=True)

    print("\n" + "-" * 80)


def example_cli_command_search():
    """CLI 명령어 검색 예제"""
    print("\n" + "=" * 80)
    print("예제 5: CLI 명령어 전용 검색")
    print("=" * 80)

    vector_store = CiscoVectorStore(
        collection_name="cisco_manuals",
        persist_directory="./data/chroma_db"
    )

    llm_service = OllamaService(model_name="llama3.1:8b")

    rag = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="google"
    )

    # CLI 명령어 검색 (한국어 설명으로)
    command_descriptions = [
        "MAC 주소 테이블 확인",
        "라우팅 테이블 보기",
        "인터페이스 설정 진입"
    ]

    for desc in command_descriptions:
        print(f"\n요청: {desc}")
        print("-" * 40)

        response = rag.query_cli_command(desc)
        print(f"답변:\n{response.answer}")


def example_toggle_translation():
    """번역 기능 토글 예제"""
    print("\n" + "=" * 80)
    print("예제 6: 번역 기능 활성화/비활성화")
    print("=" * 80)

    vector_store = CiscoVectorStore(
        collection_name="cisco_manuals",
        persist_directory="./data/chroma_db"
    )

    llm_service = OllamaService(model_name="llama3.1:8b")

    rag = create_multilingual_rag(
        vector_store=vector_store,
        llm_service=llm_service,
        translator_type="google",
        enable_translation=True
    )

    question = "What is VLAN?"

    # 번역 활성화 상태
    print("\n1. 번역 활성화 (영어 질문 → 그대로 처리)")
    print("-" * 40)
    response1 = rag.query(question)
    print(f"답변: {response1.answer[:150]}...")

    # 번역 비활성화
    print("\n2. 번역 비활성화")
    print("-" * 40)
    rag.set_translation_enabled(False)
    response2 = rag.query(question)
    print(f"답변: {response2.answer[:150]}...")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("시스코 매뉴얼 다국어 RAG 예제")
    print("=" * 80)

    # 예제 실행 선택
    print("\n실행할 예제를 선택하세요:")
    print("1. 기본 다국어 RAG")
    print("2. 이중 언어 출력")
    print("3. 다양한 번역기 비교")
    print("4. 스트리밍 응답")
    print("5. CLI 명령어 검색")
    print("6. 번역 기능 토글")
    print("0. 모든 예제 실행")

    choice = input("\n선택 (0-6): ").strip()

    try:
        if choice == "1":
            example_basic_translation()
        elif choice == "2":
            example_bilingual_output()
        elif choice == "3":
            example_translation_types()
        elif choice == "4":
            example_streaming()
        elif choice == "5":
            example_cli_command_search()
        elif choice == "6":
            example_toggle_translation()
        elif choice == "0":
            example_basic_translation()
            example_bilingual_output()
            example_translation_types()
            example_streaming()
            example_cli_command_search()
            example_toggle_translation()
        else:
            print("잘못된 선택입니다.")

    except Exception as e:
        print(f"\n오류 발생: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "=" * 80)
    print("예제 종료")
    print("=" * 80)
