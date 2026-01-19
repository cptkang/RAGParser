# tests/test_with_existing_vectorstore.py

"""
기존 IndexingPipeline으로 생성된 벡터 스토어를 사용한 RAG 테스트

실행 방법:
    pytest tests/test_with_existing_vectorstore.py -v -s

사전 조건:
    indexing_pipeline.py로 벡터 스토어가 이미 생성되어 있어야 함
"""

import pytest
import sys
import os
from pathlib import Path

# 프로젝트 루트 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vectorstore.chroma_store import CiscoVectorStore
from src.embedding.embedding_service import CiscoEmbeddingService
from src.rag.rag_chain import CiscoRAGChain, RAGResponse
from src.rag.rag_factory import RAGFactory, RAGMode, UnifiedRAGInterface


# ============================================================================
# 설정
# ============================================================================

# IndexingPipeline에서 생성한 벡터 스토어 경로
VECTORDB_DIR = "./vectordb"  # indexing_pipeline.py의 기본 경로
EMBEDDING_MODEL = "BAAI/bge-m3"  # indexing_pipeline.py에서 사용한 모델


# ============================================================================
# 벡터 스토어 존재 여부 확인
# ============================================================================

def vectorstore_exists():
    """벡터 스토어가 존재하는지 확인"""
    vectordb_path = Path(VECTORDB_DIR)
    return vectordb_path.exists() and any(vectordb_path.iterdir())


# 벡터 스토어가 없으면 테스트 스킵
pytestmark = pytest.mark.skipif(
    not vectorstore_exists(),
    reason=f"벡터 스토어가 존재하지 않음: {VECTORDB_DIR}. "
           f"먼저 indexing_pipeline.py를 실행하세요."
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture(scope="module")
def embedding_service():
    """임베딩 서비스 (IndexingPipeline과 동일한 모델 사용)"""
    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\n임베딩 디바이스: {device}")
    return CiscoEmbeddingService(
        model_name=EMBEDDING_MODEL,
        device=device
    )


@pytest.fixture(scope="module")
def vector_store(embedding_service):
    """기존 벡터 스토어 로드 (새로 인덱싱하지 않음)"""
    store = CiscoVectorStore(
        collection_name="cisco_manuals",  # IndexingPipeline 기본 컬렉션명
        persist_directory=VECTORDB_DIR,
        embedding_service=embedding_service
    )

    # 로드된 문서 수 확인
    doc_count = store.collection.count()
    print(f"\n기존 벡터 스토어 로드 완료: {doc_count}개 문서")

    if doc_count == 0:
        pytest.skip("벡터 스토어에 문서가 없습니다. indexing_pipeline.py를 먼저 실행하세요.")

    return store


@pytest.fixture
def mock_llm_service():
    """Mock LLM 서비스 (또는 실제 LLM 사용)"""
    # 실제 Ollama 사용시:
    # from src.llm.llama_service import OllamaService
    # return OllamaService(model_name="llama3.1:8b")

    class MockLLMService:
        def generate(self, prompt: str, **kwargs):
            # 검색된 컨텍스트 기반 응답
            if 'vlan' in prompt.lower():
                return "VLAN 설정 방법: configure terminal -> vlan [번호] -> name [이름]"
            elif 'route' in prompt.lower() or 'routing' in prompt.lower():
                return "라우팅 설정: ip route [목적지] [마스크] [게이트웨이]"
            elif 'interface' in prompt.lower():
                return "인터페이스 설정: interface [타입/번호] -> ip address -> no shutdown"
            return "참고 문서를 기반으로 답변합니다."

        def generate_stream(self, prompt: str, **kwargs):
            response = self.generate(prompt, **kwargs)
            for word in response.split():
                yield word + " "

    return MockLLMService()


@pytest.fixture
def rag_chain(vector_store, mock_llm_service):
    """RAG 체인"""
    return CiscoRAGChain(
        vector_store=vector_store,
        llm_service=mock_llm_service,
        top_k=5,
        score_threshold=0.3
    )


# ============================================================================
# 벡터 스토어 테스트
# ============================================================================

class TestExistingVectorStore:
    """기존 벡터 스토어 테스트"""

    def test_document_count(self, vector_store):
        """문서 개수 확인"""
        count = vector_store.collection.count()
        assert count > 0, "벡터 스토어에 문서가 없습니다"
        print(f"\n총 인덱싱된 문서: {count}개")

    def test_collection_stats(self, vector_store):
        """컬렉션 통계"""
        stats = vector_store.get_collection_stats()
        print(f"\n컬렉션 통계: {stats}")
        assert stats['total_documents'] > 0

    def test_search_vlan(self, vector_store):
        """VLAN 검색 테스트"""
        results = vector_store.search("VLAN configuration", k=5)

        print(f"\n'VLAN configuration' 검색 결과: {len(results)}개")
        for i, r in enumerate(results[:3], 1):
            print(f"  {i}. Score: {r['score']:.3f}")
            print(f"     Chapter: {r['metadata'].get('chapter', 'N/A')}")
            print(f"     Content: {r['content'][:100]}...")

        assert len(results) > 0

    def test_search_interface(self, vector_store):
        """인터페이스 검색 테스트"""
        results = vector_store.search("interface configuration", k=5)

        print(f"\n'interface configuration' 검색 결과: {len(results)}개")
        assert len(results) > 0

    def test_search_with_korean(self, vector_store):
        """한국어 검색 테스트"""
        results = vector_store.search("포트 설정 명령어", k=5)

        print(f"\n'포트 설정 명령어' 검색 결과: {len(results)}개")
        # 한국어 검색은 결과가 없을 수도 있음 (영문 문서인 경우)

    def test_metadata_filtering(self, vector_store):
        """메타데이터 필터링 테스트"""
        # 특정 장비 타입으로 필터링
        results = vector_store.search(
            "configuration",
            k=10,
            filter_metadata={"device_type": "Nexus 9000"}
        )

        print(f"\nNexus 9000 필터링 결과: {len(results)}개")

        # 필터링 결과 검증
        for r in results:
            if 'device_type' in r['metadata']:
                assert r['metadata']['device_type'] == "Nexus 9000"


# ============================================================================
# RAG 체인 테스트
# ============================================================================

class TestRAGWithExistingStore:
    """기존 벡터 스토어를 사용한 RAG 테스트"""

    def test_basic_query(self, rag_chain):
        """기본 쿼리 테스트"""
        response = rag_chain.query(
            "How to configure VLAN?",
            include_sources=True
        )

        assert isinstance(response, RAGResponse)
        assert response.answer is not None
        print(f"\n쿼리: How to configure VLAN?")
        print(f"신뢰도: {response.confidence:.2f}")
        print(f"검색된 소스: {len(response.sources)}개")
        print(f"답변: {response.answer[:200]}...")

    def test_interface_query(self, rag_chain):
        """인터페이스 설정 쿼리"""
        response = rag_chain.query(
            "show interface configuration commands",
            include_sources=True
        )

        assert response.answer is not None
        print(f"\n인터페이스 쿼리 신뢰도: {response.confidence:.2f}")

    def test_routing_query(self, rag_chain):
        """라우팅 설정 쿼리"""
        response = rag_chain.query(
            "static route configuration",
            include_sources=True
        )

        assert response.answer is not None
        print(f"\n라우팅 쿼리 신뢰도: {response.confidence:.2f}")

    def test_query_with_filter(self, rag_chain):
        """필터링된 쿼리"""
        response = rag_chain.query(
            "port configuration",
            filter_metadata={"device_type": "Nexus 9000"},
            include_sources=True
        )

        assert response.answer is not None
        print(f"\n필터링 쿼리 결과: {len(response.sources)}개 소스")


# ============================================================================
# 고급 RAG 테스트
# ============================================================================

class TestAdvancedRAGWithExistingStore:
    """고급 RAG 모드 테스트"""

    def test_rag_factory(self, vector_store, mock_llm_service):
        """RAG Factory 테스트"""
        factory = RAGFactory(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        # 기본 모드
        default_rag = factory.get_chain(RAGMode.DEFAULT)
        response = default_rag.query("VLAN configuration")

        assert response.answer is not None
        print(f"\nRAG Factory DEFAULT 모드 응답 완료")

    def test_unified_interface(self, vector_store, mock_llm_service):
        """통합 인터페이스 테스트"""
        interface = UnifiedRAGInterface(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        response = interface.query(
            "How to configure trunk port?",
            auto_mode=True
        )

        assert response.answer is not None
        print(f"\n통합 인터페이스 쿼리 완료")


# ============================================================================
# 실제 데이터 품질 테스트
# ============================================================================

class TestDataQuality:
    """인덱싱된 데이터 품질 테스트"""

    def test_search_relevance(self, vector_store):
        """검색 관련성 테스트"""
        test_queries = [
            ("VLAN", ["vlan", "virtual", "lan"]),
            ("interface", ["interface", "port", "ethernet"]),
            ("routing", ["route", "routing", "ip"]),
        ]

        print("\n검색 관련성 테스트:")
        for query, expected_keywords in test_queries:
            results = vector_store.search(query, k=3)

            if len(results) > 0:
                top_result = results[0]
                content_lower = top_result['content'].lower()
                has_keyword = any(kw in content_lower for kw in expected_keywords)

                status = "OK" if has_keyword else "WARN"
                print(f"  [{status}] '{query}': score={top_result['score']:.3f}")
            else:
                print(f"  [SKIP] '{query}': 검색 결과 없음")

    def test_metadata_completeness(self, vector_store):
        """메타데이터 완전성 테스트"""
        results = vector_store.search("configuration", k=10)

        required_fields = ['source', 'chapter']

        print("\n메타데이터 완전성:")
        for r in results[:5]:
            metadata = r['metadata']
            missing = [f for f in required_fields if f not in metadata]

            if missing:
                print(f"  [WARN] 누락된 필드: {missing}")
            else:
                print(f"  [OK] source={metadata.get('source', 'N/A')[:30]}")


# ============================================================================
# 메인 실행
# ============================================================================

if __name__ == "__main__":
    # 벡터 스토어 존재 확인
    if not vectorstore_exists():
        print(f"오류: 벡터 스토어가 존재하지 않습니다: {VECTORDB_DIR}")
        print("먼저 indexing_pipeline.py를 실행하세요:")
        print("  python src/vectorstore/indexing_pipeline.py")
        sys.exit(1)

    pytest.main([__file__, "-v", "-s"])
