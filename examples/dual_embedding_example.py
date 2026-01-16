# examples/dual_embedding_example.py

"""
이중 임베딩 전략 예제

영문 문서 전용 모델 vs 다국어 통합 모델 비교
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.embedding.dual_embedding_service import (
    DualEmbeddingService,
    UnifiedEmbeddingService,
    create_embedding_service
)
from src.embedding.model_selection import (
    ENGLISH_DOCUMENT_MODELS,
    MULTILINGUAL_MODELS,
    FINAL_RECOMMENDATION
)


def example_model_comparison():
    """모델 비교"""
    print("=" * 80)
    print("영문 문서용 모델 vs 다국어 모델 비교")
    print("=" * 80)

    print("\n[영문 전용 모델]")
    for model in ENGLISH_DOCUMENT_MODELS[:3]:
        print(f"\n{model.name} ({model.model_id})")
        print(f"  - 영어 성능: {model.english_score}/10")
        print(f"  - 기술 문서: {model.tech_domain_score}/10")
        print(f"  - 메모리: {model.memory_gb}GB")
        print(f"  - 노트: {model.notes}")

    print("\n" + "-" * 80)
    print("[다국어 모델]")
    for model in MULTILINGUAL_MODELS[:2]:
        print(f"\n{model.name} ({model.model_id})")
        print(f"  - 영어: {model.english_score}/10")
        print(f"  - 한국어: {model.korean_score}/10")
        print(f"  - 기술: {model.tech_domain_score}/10")
        print(f"  - 메모리: {model.memory_gb}GB")
        print(f"  - 노트: {model.notes}")


def example_dual_embedding():
    """이중 임베딩 서비스 예제"""
    print("\n" + "=" * 80)
    print("전략 1: 이중 임베딩 (최고 성능)")
    print("=" * 80)

    # 영문 전용 모델 사용
    service = DualEmbeddingService(
        document_model="BAAI/bge-large-en-v1.5"
    )

    print("\n모델 정보:")
    info = service.get_model_info()
    for key, value in info.items():
        print(f"  {key}: {value}")

    # 샘플 문서 임베딩
    from langchain_core.documents import Document

    sample_docs = [
        Document(
            page_content="Configure VLAN 10 on the switch using the vlan command.",
            metadata={"chunk_type": "text"}
        ),
        Document(
            page_content="""Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name Sales""",
            metadata={"chunk_type": "cli_command"}
        )
    ]

    print("\n문서 임베딩 중...")
    doc_embeddings = service.embed_documents(sample_docs, show_progress=False)
    print(f"임베딩 완료: {len(doc_embeddings)}개 문서")
    print(f"차원: {doc_embeddings[0]['embedding'].shape}")

    # 샘플 쿼리 (번역된 영어)
    queries = [
        "How to configure VLAN?",
        "Show VLAN configuration command"
    ]

    print("\n쿼리 임베딩 중...")
    for query in queries:
        query_emb = service.embed_query(query)
        print(f"  '{query}' → 차원: {query_emb.shape}")

        # 유사도 계산
        similarities = service.compute_similarity(
            query_emb,
            [doc['embedding'] for doc in doc_embeddings]
        )
        print(f"    유사도: {similarities}")


def example_unified_embedding():
    """통합 임베딩 서비스 예제"""
    print("\n" + "=" * 80)
    print("전략 2: 통합 임베딩 (균형)")
    print("=" * 80)

    # 다국어 모델 사용
    service = UnifiedEmbeddingService(
        model_name="BAAI/bge-m3"
    )

    print("\n모델 정보:")
    info = service.get_model_info()
    for key, value in info.items():
        print(f"  {key}: {value}")

    # 샘플 문서
    from langchain_core.documents import Document

    sample_docs = [
        Document(
            page_content="Configure VLAN 10 on the switch using the vlan command.",
            metadata={"chunk_type": "text"}
        )
    ]

    print("\n문서 임베딩 중...")
    doc_embeddings = service.embed_documents(sample_docs, show_progress=False)
    print(f"임베딩 완료: {len(doc_embeddings)}개 문서")

    # 다국어 쿼리
    queries = [
        "How to configure VLAN?",  # 영어
        "VLAN 설정 방법"  # 한국어 (다국어 모델은 직접 지원)
    ]

    print("\n쿼리 임베딩 중...")
    for query in queries:
        query_emb = service.embed_query(query)
        print(f"  '{query}' → 차원: {query_emb.shape}")


def example_factory():
    """팩토리 함수 사용"""
    print("\n" + "=" * 80)
    print("팩토리 함수로 서비스 생성")
    print("=" * 80)

    # 전략 1: 이중 임베딩
    print("\n[이중 임베딩]")
    service_dual = create_embedding_service(
        strategy="dual",
        document_model="BAAI/bge-large-en-v1.5"
    )
    print(f"생성됨: {type(service_dual).__name__}")
    print(f"정보: {service_dual.get_model_info()}")

    # 전략 2: 통합 임베딩
    print("\n[통합 임베딩]")
    service_unified = create_embedding_service(
        strategy="unified",
        document_model="BAAI/bge-m3"
    )
    print(f"생성됨: {type(service_unified).__name__}")
    print(f"정보: {service_unified.get_model_info()}")


def example_performance_comparison():
    """성능 비교"""
    print("\n" + "=" * 80)
    print("성능 비교 시뮬레이션")
    print("=" * 80)

    import time
    from langchain_core.documents import Document

    # 샘플 문서
    sample_docs = [
        Document(
            page_content=f"Network configuration document {i}. This describes VLAN settings.",
            metadata={"chunk_type": "text"}
        )
        for i in range(100)
    ]

    strategies = [
        ("dual", "BAAI/bge-base-en-v1.5"),  # 빠른 영문 모델
        ("unified", "BAAI/bge-m3")  # 다국어 모델
    ]

    for strategy, model in strategies:
        print(f"\n[{strategy.upper()} - {model}]")

        try:
            service = create_embedding_service(
                strategy=strategy,
                document_model=model
            )

            # 임베딩 속도 측정
            start = time.time()
            embeddings = service.embed_documents(sample_docs, show_progress=False)
            elapsed = time.time() - start

            print(f"  문서 수: {len(sample_docs)}")
            print(f"  임베딩 시간: {elapsed:.2f}초")
            print(f"  문서당: {elapsed/len(sample_docs)*1000:.1f}ms")
            print(f"  차원: {embeddings[0]['embedding'].shape[0]}")

        except Exception as e:
            print(f"  오류: {e}")


def show_recommendation():
    """권장 사항 출력"""
    print("\n" + "=" * 80)
    print("최종 권장 사항")
    print("=" * 80)
    print(FINAL_RECOMMENDATION)


if __name__ == "__main__":
    print("\n시스코 매뉴얼 이중 임베딩 전략 예제")
    print("=" * 80)

    print("\n실행할 예제를 선택하세요:")
    print("1. 모델 비교")
    print("2. 이중 임베딩 (영문 전용)")
    print("3. 통합 임베딩 (다국어)")
    print("4. 팩토리 함수")
    print("5. 성능 비교")
    print("6. 권장 사항")
    print("0. 모든 예제 실행")

    choice = input("\n선택 (0-6): ").strip()

    try:
        if choice == "1":
            example_model_comparison()
        elif choice == "2":
            example_dual_embedding()
        elif choice == "3":
            example_unified_embedding()
        elif choice == "4":
            example_factory()
        elif choice == "5":
            example_performance_comparison()
        elif choice == "6":
            show_recommendation()
        elif choice == "0":
            example_model_comparison()
            example_dual_embedding()
            example_unified_embedding()
            example_factory()
            example_performance_comparison()
            show_recommendation()
        else:
            print("잘못된 선택입니다.")

    except Exception as e:
        print(f"\n오류 발생: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "=" * 80)
    print("예제 종료")
    print("=" * 80)
