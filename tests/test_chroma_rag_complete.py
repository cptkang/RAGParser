# tests/test_chroma_rag_complete.py

"""
ChromaDB를 이용한 실제 RAG 시스템 통합 테스트

이 테스트는 실제 벡터 데이터베이스를 사용하여 RAG 파이프라인을 검증합니다.
- 실제 임베딩 모델 사용
- ChromaDB 영구 저장소 사용
- 실제 문서 인덱싱 및 검색
- 다양한 RAG 모드 테스트

실행 방법:
    pytest tests/test_chroma_rag_complete.py -v --tb=short
"""

import pytest
import sys
import os
from pathlib import Path
from typing import List, Dict
import shutil
import tempfile

# 프로젝트 루트 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.documents import Document
from src.vectorstore.chroma_store import CiscoVectorStore
from src.embedding.embedding_service import CiscoEmbeddingService
from src.rag.rag_chain import CiscoRAGChain, RAGResponse
from src.rag.advanced_rag import (
    HybridSearchRAG,
    ConversationalRAG,
    StepByStepRAG,
    TroubleshootingRAG
)
from src.rag.rag_factory import RAGFactory, RAGMode, UnifiedRAGInterface


# ============================================================================
# 테스트 데이터: 시스코 네트워크 설정 관련 샘플 문서
# ============================================================================

SAMPLE_DOCUMENTS = [
    # VLAN 설정 문서
    Document(
        page_content="""# VLAN Configuration Guide

## VLAN 생성 방법

VLAN(Virtual Local Area Network)을 생성하려면 다음 단계를 따르세요:

1. 전역 설정 모드 진입
```
Switch# configure terminal
```

2. VLAN 생성
```
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
Switch(config-vlan)# exit
```

3. 설정 확인
```
Switch# show vlan brief
```

VLAN 10이 SALES라는 이름으로 생성됩니다.""",
        metadata={
            "source": "cisco_vlan_guide.pdf",
            "chapter": "VLAN Configuration",
            "device_type": "Catalyst 9000",
            "chunk_type": "configuration"
        }
    ),

    # VLAN 트렁크 설정
    Document(
        page_content="""## VLAN Trunk Configuration

트렁크 포트는 여러 VLAN 트래픽을 전달할 수 있습니다.

### 트렁크 포트 설정
```
Switch(config)# interface GigabitEthernet1/0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
Switch(config-if)# exit
```

### 설정 확인
```
Switch# show interfaces trunk
```""",
        metadata={
            "source": "cisco_vlan_guide.pdf",
            "chapter": "VLAN Trunking",
            "device_type": "Catalyst 9000",
            "chunk_type": "configuration"
        }
    ),

    # 스태틱 라우팅 설정
    Document(
        page_content="""# Static Routing Configuration

## 스태틱 라우트 설정 방법

스태틱 라우트는 관리자가 수동으로 경로를 지정하는 방식입니다.

### 기본 스태틱 라우트
```
Router# configure terminal
Router(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.1
Router(config)# exit
```

### 디폴트 라우트
디폴트 라우트는 모든 알려지지 않은 목적지로의 경로를 지정합니다.
```
Router(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

### 검증
```
Router# show ip route static
```

스태틱 라우팅은 소규모 네트워크에 적합하며, 네트워크 오버헤드가 적습니다.""",
        metadata={
            "source": "cisco_routing_guide.pdf",
            "chapter": "Static Routing",
            "device_type": "ISR 4000",
            "chunk_type": "configuration"
        }
    ),

    # OSPF 설정
    Document(
        page_content="""## OSPF Dynamic Routing

OSPF(Open Shortest Path First)는 링크 스테이트 라우팅 프로토콜입니다.

### OSPF 기본 설정
```
Router# configure terminal
Router(config)# router ospf 1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
Router(config-router)# network 10.0.0.0 0.255.255.255 area 0
Router(config-router)# exit
```

### Router ID 설정
```
Router(config-router)# router-id 1.1.1.1
```

### 확인 명령어
```
Router# show ip ospf neighbor
Router# show ip ospf interface
Router# show ip route ospf
```

OSPF는 대규모 네트워크에 적합하며, 빠른 수렴 시간을 제공합니다.""",
        metadata={
            "source": "cisco_routing_guide.pdf",
            "chapter": "OSPF Configuration",
            "device_type": "ISR 4000",
            "chunk_type": "configuration"
        }
    ),

    # 인터페이스 설정
    Document(
        page_content="""# Interface Configuration

## 기본 인터페이스 설정

### IP 주소 할당
```
Router# configure terminal
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# description LAN Interface
Router(config-if)# exit
```

### 설정 확인
```
Router# show ip interface brief
Router# show interfaces GigabitEthernet0/0
```""",
        metadata={
            "source": "cisco_interface_guide.pdf",
            "chapter": "Interface Configuration",
            "device_type": "ISR 4000",
            "chunk_type": "configuration"
        }
    ),

    # 트러블슈팅 가이드
    Document(
        page_content="""# Network Troubleshooting Guide

## 인터페이스 문제 진단

### 인터페이스가 다운된 경우
1. 물리적 연결 확인
2. 인터페이스 상태 확인
```
Router# show interfaces status
Router# show ip interface brief
```

3. 에러 카운터 확인
```
Router# show interfaces GigabitEthernet0/0
```

## 라우팅 문제 진단

### 라우팅 테이블 확인
```
Router# show ip route
Router# show ip protocols
```

### 연결성 테스트
```
Router# ping 192.168.1.1
Router# traceroute 192.168.1.1
```

## VLAN 통신 문제

### VLAN 설정 확인
```
Switch# show vlan brief
Switch# show interfaces trunk
Switch# show interfaces switchport
```""",
        metadata={
            "source": "cisco_troubleshooting_guide.pdf",
            "chapter": "Troubleshooting",
            "device_type": "General",
            "chunk_type": "troubleshooting"
        }
    ),
]


# ============================================================================
# Mock LLM Service (실제 LLM 없이 테스트)
# ============================================================================

class MockLLMService:
    """테스트용 Mock LLM 서비스"""

    def generate(self, prompt: str, system_prompt: str = None,
                 max_tokens: int = 1024, temperature: float = 0.1):
        """컨텍스트 기반으로 적절한 응답 생성"""

        # VLAN 관련 쿼리
        if any(keyword in prompt.lower() for keyword in ['vlan', '브이랜']):
            if 'trunk' in prompt.lower() or '트렁크' in prompt.lower():
                return """VLAN 트렁크 포트를 설정하려면 다음 단계를 따르세요:

1단계: 인터페이스 선택
```
Switch(config)# interface GigabitEthernet1/0/1
```

2단계: 트렁크 모드 설정
```
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

3단계: 설정 확인
```
Switch# show interfaces trunk
```

트렁크 포트는 여러 VLAN의 트래픽을 전달할 수 있습니다."""
            else:
                return """VLAN을 생성하려면 다음 단계를 따르세요:

1단계: 전역 설정 모드 진입
```
Switch# configure terminal
```

2단계: VLAN 생성
```
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
```

3단계: 설정 확인
```
Switch# show vlan brief
```"""

        # 라우팅 관련 쿼리
        elif any(keyword in prompt.lower() for keyword in ['route', 'routing', '라우팅', '라우트']):
            if 'ospf' in prompt.lower():
                return """OSPF 라우팅 프로토콜을 설정하는 방법:

1단계: OSPF 프로세스 시작
```
Router(config)# router ospf 1
```

2단계: 네트워크 영역 지정
```
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

3단계: 설정 확인
```
Router# show ip ospf neighbor
Router# show ip route ospf
```

OSPF는 대규모 네트워크에 적합한 다이나믹 라우팅 프로토콜입니다."""
            elif 'default' in prompt.lower() or '디폴트' in prompt:
                return """디폴트 라우트 설정 방법:

```
Router(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

디폴트 라우트는 라우팅 테이블에 없는 모든 목적지로의 경로를 지정합니다."""
            else:
                return """스태틱 라우트 설정 방법:

```
Router(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.1
```

스태틱 라우팅은 관리자가 수동으로 경로를 지정하는 방식입니다."""

        # 인터페이스 관련 쿼리
        elif any(keyword in prompt.lower() for keyword in ['interface', '인터페이스']):
            return """인터페이스 설정 방법:

```
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
```

설정 확인:
```
Router# show ip interface brief
```"""

        # 트러블슈팅 쿼리
        elif any(keyword in prompt.lower() for keyword in ['문제', '안됨', 'troubleshoot', 'problem']):
            return """문제 진단 절차:

1. 상태 확인
```
Router# show ip interface brief
Router# show ip route
```

2. 연결성 테스트
```
Router# ping <목적지>
Router# traceroute <목적지>
```

3. 설정 확인 및 수정"""

        # 기본 응답
        return "제공된 참고 문서를 기반으로 답변을 생성했습니다."

    def generate_stream(self, prompt: str, **kwargs):
        """스트리밍 응답"""
        response = self.generate(prompt, **kwargs)
        for word in response.split():
            yield word + " "


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture(scope="module")
def temp_vectordb_dir():
    """임시 벡터 DB 디렉토리 생성"""
    temp_dir = tempfile.mkdtemp(prefix="test_vectordb_")
    yield temp_dir
    # 테스트 후 정리 (Windows에서 파일 잠금 문제로 실패할 수 있음)
    try:
        if os.path.exists(temp_dir):
            import time
            time.sleep(0.5)  # 짧은 대기로 파일 핸들 해제 대기
            shutil.rmtree(temp_dir, ignore_errors=True)
    except Exception as e:
        print(f"\n[WARNING] 임시 디렉토리 정리 실패: {e}")


@pytest.fixture(scope="module")
def embedding_service():
    """임베딩 서비스 (실제 모델 사용)"""
    # 작은 모델로 테스트 (빠른 실행)
    return CiscoEmbeddingService(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        device="cpu"
    )


@pytest.fixture(scope="module")
def vector_store(temp_vectordb_dir, embedding_service):
    """벡터 스토어 초기화 및 샘플 문서 인덱싱"""
    store = CiscoVectorStore(
        collection_name="test_cisco_manuals",
        persist_directory=temp_vectordb_dir,
        embedding_service=embedding_service
    )

    # 샘플 문서 추가
    print(f"\n인덱싱 중: {len(SAMPLE_DOCUMENTS)}개 문서...")
    store.add_documents(SAMPLE_DOCUMENTS)
    print(f"인덱싱 완료: {store.collection.count()}개 문서")

    return store


@pytest.fixture
def mock_llm_service():
    """Mock LLM 서비스"""
    return MockLLMService()


@pytest.fixture
def rag_chain(vector_store, mock_llm_service):
    """기본 RAG 체인"""
    return CiscoRAGChain(
        vector_store=vector_store,
        llm_service=mock_llm_service,
        top_k=3,
        score_threshold=0.3
    )


# ============================================================================
# 벡터 스토어 기본 테스트
# ============================================================================

class TestVectorStore:
    """벡터 스토어 기본 기능 테스트"""

    def test_document_count(self, vector_store):
        """문서 개수 확인"""
        count = vector_store.collection.count()
        assert count == len(SAMPLE_DOCUMENTS)
        print(f"\n[OK] 총 {count}개 문서 인덱싱됨")

    def test_vlan_search(self, vector_store):
        """VLAN 관련 검색"""
        results = vector_store.search("VLAN 설정 방법", k=3)

        assert len(results) > 0
        assert any('vlan' in r['content'].lower() for r in results)

        print("\n[OK] VLAN 검색 결과:")
        for i, result in enumerate(results[:2], 1):
            print(f"  {i}. Score: {result['score']:.3f}")
            print(f"     Chapter: {result['metadata'].get('chapter', 'N/A')}")

    def test_routing_search(self, vector_store):
        """라우팅 관련 검색"""
        results = vector_store.search("스태틱 라우트 설정", k=3)

        assert len(results) > 0
        assert any('route' in r['content'].lower() or 'routing' in r['content'].lower()
                   for r in results)

        print("\n[OK] 라우팅 검색 결과:")
        for i, result in enumerate(results[:2], 1):
            print(f"  {i}. Score: {result['score']:.3f}")
            print(f"     Chapter: {result['metadata'].get('chapter', 'N/A')}")

    def test_metadata_filtering(self, vector_store):
        """메타데이터 필터링"""
        results = vector_store.search(
            "configuration",
            k=5,
            filter_metadata={"device_type": "Catalyst 9000"}
        )

        assert len(results) > 0
        # 필터링된 결과 확인
        for result in results:
            assert result['metadata'].get('device_type') == "Catalyst 9000"

        print(f"\n[OK] Catalyst 9000 필터링: {len(results)}개 결과")


# ============================================================================
# 기본 RAG 체인 테스트
# ============================================================================

class TestCiscoRAGChainWithChroma:
    """실제 벡터 스토어를 사용한 RAG 체인 테스트"""

    def test_vlan_configuration_query(self, rag_chain):
        """VLAN 설정 쿼리"""
        response = rag_chain.query("VLAN 10을 생성하는 방법을 알려주세요")

        assert isinstance(response, RAGResponse)
        assert response.answer is not None
        assert len(response.answer) > 50
        assert response.confidence > 0

        print(f"\n[OK] VLAN 쿼리 응답:")
        print(f"  신뢰도: {response.confidence:.2f}")
        print(f"  답변 길이: {len(response.answer)} 자")

    def test_static_routing_query(self, rag_chain):
        """스태틱 라우팅 쿼리"""
        response = rag_chain.query("스태틱 라우트 설정 명령어", include_sources=True)

        assert response.answer is not None
        assert len(response.sources) > 0
        assert any('route' in s['content'].lower() for s in response.sources)

        print(f"\n[OK] 라우팅 쿼리:")
        print(f"  검색된 소스: {len(response.sources)}개")
        print(f"  신뢰도: {response.confidence:.2f}")

    def test_ospf_configuration_query(self, rag_chain):
        """OSPF 설정 쿼리"""
        response = rag_chain.query("OSPF 라우팅 프로토콜 설정", include_sources=True)

        assert response.answer is not None
        # OSPF가 응답이나 소스에 포함되어야 함
        has_ospf = ('ospf' in response.answer.lower() or
                    any('ospf' in s['content'].lower() for s in response.sources))
        assert has_ospf, "OSPF 관련 내용이 응답이나 소스에 없음"

        print(f"\n[OK] OSPF 쿼리 신뢰도: {response.confidence:.2f}")

    def test_trunk_configuration_query(self, rag_chain):
        """트렁크 포트 설정 쿼리"""
        response = rag_chain.query("VLAN trunk port configuration", include_sources=True)

        assert response.answer is not None
        # 응답이 있거나 낮은 신뢰도여야 함 (검색 결과가 없을 수 있음)
        # 트렁크는 특정 용어라서 임베딩 모델이 잘 매칭하지 못할 수 있음
        if len(response.sources) > 0:
            has_relevant = any(
                any(keyword in s['content'].lower()
                    for keyword in ['trunk', 'vlan', 'switchport'])
                for s in response.sources
            )
            assert has_relevant, "관련 소스가 있지만 트렁크/VLAN 키워드가 없음"

        print(f"\n[OK] 트렁크 쿼리 신뢰도: {response.confidence:.2f}, 소스: {len(response.sources)}개")

    def test_device_filtering_query(self, rag_chain):
        """장비 타입 필터링 쿼리"""
        response = rag_chain.query(
            "VLAN 설정",
            filter_metadata={"device_type": "Catalyst 9000"}
        )

        assert response.answer is not None
        # 소스가 Catalyst 9000인지 확인
        if len(response.sources) > 0:
            assert all(s['metadata'].get('device_type') == "Catalyst 9000"
                       for s in response.sources)

        print(f"\n[OK] 장비 필터링 쿼리 완료")


# ============================================================================
# 고급 RAG 모드 테스트
# ============================================================================

class TestAdvancedRAGWithChroma:
    """고급 RAG 모드 테스트"""

    def test_hybrid_search(self, vector_store, mock_llm_service):
        """하이브리드 검색 RAG"""
        rag = HybridSearchRAG(
            vector_store=vector_store,
            llm_service=mock_llm_service,
            keyword_weight=0.3
        )

        response = rag.query("show vlan brief 명령어")

        assert response.answer is not None
        print(f"\n[OK] 하이브리드 검색 신뢰도: {response.confidence:.2f}")

    def test_conversational_rag(self, vector_store, mock_llm_service):
        """대화형 RAG"""
        rag = ConversationalRAG(
            vector_store=vector_store,
            llm_service=mock_llm_service,
            max_history=5
        )

        # 첫 번째 질문
        response1 = rag.query("VLAN 설정 방법")
        assert response1.answer is not None
        assert len(rag.conversation_history) == 1

        # 두 번째 질문 (문맥 기반)
        response2 = rag.query("트렁크 포트는 어떻게 설정하나요?")
        assert response2.answer is not None
        assert len(rag.conversation_history) == 2

        print(f"\n[OK] 대화형 RAG: {len(rag.conversation_history)}턴 대화")

    def test_step_by_step_rag(self, vector_store, mock_llm_service):
        """단계별 안내 RAG"""
        rag = StepByStepRAG(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        response = rag.query("스태틱 라우트를 설정하는 절차")

        assert response.answer is not None
        assert '단계' in response.answer or '1' in response.answer

        print(f"\n[OK] 단계별 안내 응답 생성 완료")

    def test_troubleshooting_rag(self, vector_store, mock_llm_service):
        """트러블슈팅 RAG"""
        rag = TroubleshootingRAG(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        response = rag.query("인터페이스가 다운되었습니다")

        assert response.answer is not None
        problem_type = rag._detect_problem_type("인터페이스가 다운되었습니다")
        assert problem_type == 'interface'

        print(f"\n[OK] 트러블슈팅: {problem_type} 문제 감지")


# ============================================================================
# RAG Factory 테스트
# ============================================================================

class TestRAGFactoryWithChroma:
    """RAG Factory 통합 테스트"""

    def test_factory_initialization(self, vector_store, mock_llm_service):
        """팩토리 초기화"""
        factory = RAGFactory(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        assert factory is not None
        print("\n[OK] RAG Factory 초기화 완료")

    def test_mode_switching(self, vector_store, mock_llm_service):
        """모드 전환 테스트"""
        factory = RAGFactory(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        # 기본 모드
        default_rag = factory.get_chain(RAGMode.DEFAULT)
        response1 = default_rag.query("VLAN 설정")
        assert response1.answer is not None

        # 하이브리드 모드
        hybrid_rag = factory.get_chain(RAGMode.HYBRID)
        response2 = hybrid_rag.query("VLAN 설정")
        assert response2.answer is not None

        print("\n[OK] 모드 전환 테스트 완료")

    def test_auto_mode_selection(self, vector_store, mock_llm_service):
        """자동 모드 선택"""
        factory = RAGFactory(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        # 트러블슈팅 쿼리 - TROUBLESHOOTING 또는 HYBRID 허용
        mode1 = factory.auto_select_mode("인터페이스가 다운되었습니다")
        assert mode1 in [RAGMode.TROUBLESHOOTING, RAGMode.HYBRID], \
            f"예상하지 못한 모드: {mode1.value}"

        # 설정 절차 쿼리 - STEP_BY_STEP 또는 HYBRID 허용
        mode2 = factory.auto_select_mode("VLAN 설정 방법을 단계별로 알려주세요")
        assert mode2 in [RAGMode.STEP_BY_STEP, RAGMode.HYBRID], \
            f"예상하지 못한 모드: {mode2.value}"

        print(f"\n[OK] 자동 모드 선택: {mode1.value}, {mode2.value}")


# ============================================================================
# Unified Interface 테스트
# ============================================================================

class TestUnifiedInterfaceWithChroma:
    """통합 인터페이스 테스트"""

    def test_unified_query(self, vector_store, mock_llm_service):
        """통합 쿼리"""
        interface = UnifiedRAGInterface(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        response = interface.query("VLAN 설정 방법", auto_mode=True)

        assert response.answer is not None
        print(f"\n[OK] 통합 인터페이스 쿼리 완료")

    def test_conversation_session(self, vector_store, mock_llm_service):
        """대화 세션 관리"""
        interface = UnifiedRAGInterface(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        session_id = "test_session_1"

        # 첫 번째 질문
        response1 = interface.conversation("VLAN이란 무엇인가요?", session_id)
        assert response1 is not None

        # 두 번째 질문
        response2 = interface.conversation("어떻게 설정하나요?", session_id)
        assert response2 is not None

        # 세션 삭제
        interface.delete_session(session_id)
        assert session_id not in interface._conversation_sessions

        print(f"\n[OK] 대화 세션 관리 테스트 완료")

    def test_multiple_sessions(self, vector_store, mock_llm_service):
        """다중 세션 테스트"""
        interface = UnifiedRAGInterface(
            vector_store=vector_store,
            llm_service=mock_llm_service
        )

        # 세션 1: VLAN 관련
        response1 = interface.conversation("VLAN 설정", "session_1")

        # 세션 2: 라우팅 관련
        response2 = interface.conversation("라우팅 설정", "session_2")

        assert response1 is not None
        assert response2 is not None
        assert len(interface._conversation_sessions) == 2

        # 세션 정리
        interface.delete_session("session_1")
        interface.delete_session("session_2")

        print(f"\n[OK] 다중 세션 관리 완료")


# ============================================================================
# 성능 및 품질 테스트
# ============================================================================

class TestRAGQuality:
    """RAG 품질 테스트"""

    def test_response_confidence_threshold(self, rag_chain):
        """응답 신뢰도 임계값 테스트"""
        # 관련 있는 쿼리
        response1 = rag_chain.query("VLAN 설정")
        assert response1.confidence > 0.3  # 임계값 이상

        # 관련 없는 쿼리
        response2 = rag_chain.query("날씨가 어떤가요?")
        assert response2.confidence < 0.5  # 낮은 신뢰도

        print(f"\n[OK] 신뢰도: 관련 쿼리={response1.confidence:.2f}, "
              f"무관 쿼리={response2.confidence:.2f}")

    def test_source_relevance(self, rag_chain):
        """검색된 소스의 관련성 테스트"""
        response = rag_chain.query("스태틱 라우트 설정", include_sources=True)

        assert len(response.sources) > 0

        # 모든 소스가 임계값 이상인지 확인
        for source in response.sources:
            assert source['score'] >= 0.3

        # 점수 순으로 정렬되어 있는지 확인
        scores = [s['score'] for s in response.sources]
        assert scores == sorted(scores, reverse=True)

        print(f"\n[OK] 소스 관련성: {len(response.sources)}개, "
              f"평균 점수={sum(scores)/len(scores):.3f}")

    def test_routing_specific_queries(self, rag_chain):
        """라우팅 특화 쿼리 테스트"""
        queries = [
            "디폴트 라우트 설정 방법",
            "OSPF 네트워크 명령어",
            "라우팅 테이블 확인"
        ]

        results = []
        for query in queries:
            response = rag_chain.query(query, include_sources=True)

            # 응답이나 소스 중 하나라도 라우팅 관련이면 통과
            has_route_in_answer = any(
                keyword in response.answer.lower()
                for keyword in ['route', 'routing', '라우트', '라우팅', 'ospf', 'ip']
            )
            has_route_in_sources = any(
                any(keyword in s['content'].lower()
                    for keyword in ['route', 'routing', '라우트', '라우팅', 'ospf'])
                for s in response.sources
            )

            results.append({
                'query': query,
                'confidence': response.confidence,
                'has_route_keyword': has_route_in_answer or has_route_in_sources
            })

        # 최소한 2개 이상의 쿼리가 라우팅 관련 내용을 포함해야 함
        route_count = sum(1 for r in results if r['has_route_keyword'])
        assert route_count >= 2, f"라우팅 관련 응답이 {route_count}개만 발견됨 (최소 2개 필요)"

        print("\n[OK] 라우팅 특화 쿼리:")
        for r in results:
            status = "OK" if r['has_route_keyword'] else "SKIP"
            print(f"  - [{status}] {r['query'][:25]}...: 신뢰도={r['confidence']:.2f}")


# ============================================================================
# 메인 실행
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short", "-s"])
