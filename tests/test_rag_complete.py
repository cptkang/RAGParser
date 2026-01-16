# tests/test_rag_complete.py

import pytest
from unittest.mock import Mock, MagicMock
import sys
import os

# 프로젝트 루트 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_chain import CiscoRAGChain, RAGResponse, ReRankingRAGChain
from src.rag.advanced_rag import (
    HybridSearchRAG,
    ConversationalRAG,
    StepByStepRAG,
    TroubleshootingRAG
)
from src.rag.rag_factory import RAGFactory, RAGMode, UnifiedRAGInterface


class MockVectorStore:
    """테스트용 Mock 벡터 스토어"""

    def search(self, query: str, k: int = 5, filter_metadata=None):
        # VLAN 관련 쿼리
        if 'vlan' in query.lower():
            return [
                {
                    'content': 'VLAN 설정: Switch(config)# vlan 10\nSwitch(config-vlan)# name SALES',
                    'score': 0.85,
                    'metadata': {'chapter': 'VLAN Configuration', 'chunk_type': 'cli_command'}
                },
                {
                    'content': 'VLAN은 논리적 네트워크 분할 기술입니다.',
                    'score': 0.75,
                    'metadata': {'chapter': 'VLAN Overview', 'chunk_type': 'text'}
                }
            ]
        # 라우팅 관련 쿼리
        elif any(keyword in query.lower() for keyword in ['route', 'routing', '라우팅', '라우트', '경로']):
            return [
                {
                    'content': '''스태틱 라우트 설정 방법:
Router(config)# ip route <목적지_네트워크> <서브넷_마스크> <넥스트홉_IP>
예: Router(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.1''',
                    'score': 0.90,
                    'metadata': {'chapter': 'Static Routing Configuration', 'chunk_type': 'cli_command'}
                },
                {
                    'content': '''디폴트 라우트 설정:
Router(config)# ip route 0.0.0.0 0.0.0.0 <게이트웨이_IP>
예: Router(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.1''',
                    'score': 0.88,
                    'metadata': {'chapter': 'Default Route Configuration', 'chunk_type': 'cli_command'}
                },
                {
                    'content': '''라우팅 테이블 확인 명령어:
- show ip route: 전체 라우팅 테이블 확인
- show ip route static: 스태틱 라우트만 확인
- show ip route summary: 라우팅 테이블 요약''',
                    'score': 0.82,
                    'metadata': {'chapter': 'Routing Verification', 'chunk_type': 'cli_command'}
                },
                {
                    'content': '''라우팅은 패킷을 목적지까지 전달하는 경로 결정 프로세스입니다.
스태틱 라우팅은 관리자가 수동으로 경로를 설정하며, 소규모 네트워크에 적합합니다.
다이나믹 라우팅은 라우팅 프로토콜(OSPF, EIGRP, BGP)을 사용하여 자동으로 경로를 학습합니다.''',
                    'score': 0.78,
                    'metadata': {'chapter': 'Routing Overview', 'chunk_type': 'text'}
                }
            ]
        # OSPF 관련 쿼리
        elif 'ospf' in query.lower():
            return [
                {
                    'content': '''OSPF 기본 설정:
Router(config)# router ospf <프로세스_ID>
Router(config-router)# network <네트워크> <와일드카드_마스크> area <area_번호>
예:
Router(config)# router ospf 1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0''',
                    'score': 0.92,
                    'metadata': {'chapter': 'OSPF Configuration', 'chunk_type': 'cli_command'}
                },
                {
                    'content': 'OSPF는 링크 스테이트 라우팅 프로토콜로 대규모 네트워크에 적합합니다.',
                    'score': 0.75,
                    'metadata': {'chapter': 'OSPF Overview', 'chunk_type': 'text'}
                }
            ]
        # 라우팅 트러블슈팅 쿼리
        elif any(keyword in query.lower() for keyword in ['라우팅 문제', 'routing 문제', '경로 문제']):
            return [
                {
                    'content': '''라우팅 문제 진단 명령어:
1. show ip route - 라우팅 테이블 확인
2. show ip protocols - 라우팅 프로토콜 상태
3. show ip interface brief - 인터페이스 상태
4. ping <목적지_IP> - 연결성 테스트
5. traceroute <목적지_IP> - 경로 추적''',
                    'score': 0.87,
                    'metadata': {'chapter': 'Routing Troubleshooting', 'chunk_type': 'cli_command'}
                }
            ]
        # 트러블슈팅 쿼리
        elif '문제' in query or '안됨' in query:
            return [
                {
                    'content': 'show interface status로 포트 상태 확인',
                    'score': 0.80,
                    'metadata': {'chapter': 'Troubleshooting', 'chunk_type': 'cli_command'}
                }
            ]
        return []


class MockLLMService:
    """테스트용 Mock LLM 서비스"""

    def generate(self, prompt: str, system_prompt: str = None,
                 max_tokens: int = 1024, temperature: float = 0.1):
        if 'VLAN' in prompt or 'vlan' in prompt:
            return """VLAN 10을 생성하려면 다음 단계를 따르세요:

1단계: 전역 설정 모드 진입
```
Switch# configure terminal
```

2단계: VLAN 생성
```
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
Switch(config-vlan)# exit
```

이렇게 하면 VLAN 10이 SALES라는 이름으로 생성됩니다."""

        elif any(keyword in prompt.lower() for keyword in ['route', 'routing', '라우팅', '라우트', '경로']):
            if 'ospf' in prompt.lower():
                return """OSPF 라우팅 프로토콜을 설정하려면 다음 단계를 따르세요:

1단계: OSPF 프로세스 시작
```
Router# configure terminal
Router(config)# router ospf 1
```

2단계: 네트워크 영역 지정
```
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
Router(config-router)# network 10.0.0.0 0.0.0.255 area 0
```

3단계: 설정 확인
```
Router# show ip ospf neighbor
Router# show ip route ospf
```

OSPF는 링크 스테이트 라우팅 프로토콜로 대규모 네트워크에 적합하며, 빠른 수렴 시간과 계층적 구조를 지원합니다."""

            elif '디폴트' in prompt or 'default' in prompt.lower():
                return """디폴트 라우트를 설정하려면 다음 명령어를 사용하세요:

```
Router# configure terminal
Router(config)# ip route 0.0.0.0 0.0.0.0 <게이트웨이_IP>
```

예시:
```
Router(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

디폴트 라우트는 라우팅 테이블에 명시적으로 정의되지 않은 모든 목적지에 대한 경로를 지정합니다. 주로 인터넷 연결이나 상위 네트워크로의 라우팅에 사용됩니다."""

            else:
                return """스태틱 라우트를 설정하려면 다음 단계를 따르세요:

1단계: 전역 설정 모드 진입
```
Router# configure terminal
```

2단계: 스태틱 라우트 추가
```
Router(config)# ip route <목적지_네트워크> <서브넷_마스크> <넥스트홉_IP>
```

예시:
```
Router(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.1
```

3단계: 설정 확인
```
Router# show ip route static
```

스태틱 라우팅은 소규모 네트워크나 백업 경로로 사용하기 적합합니다."""

        return "관련 정보를 찾을 수 없습니다."

    def generate_stream(self, prompt: str, **kwargs):
        response = self.generate(prompt, **kwargs)
        for word in response.split():
            yield word + " "


@pytest.fixture
def mock_vector_store():
    return MockVectorStore()


@pytest.fixture
def mock_llm_service():
    return MockLLMService()


@pytest.fixture
def rag_chain(mock_vector_store, mock_llm_service):
    return CiscoRAGChain(
        vector_store=mock_vector_store,
        llm_service=mock_llm_service,
        top_k=5,
        score_threshold=0.5
    )


class TestCiscoRAGChain:
    """기본 RAG 체인 테스트"""

    def test_basic_query(self, rag_chain):
        """기본 쿼리 테스트"""
        response = rag_chain.query("VLAN 10 설정 방법")

        assert isinstance(response, RAGResponse)
        assert response.answer is not None
        assert len(response.answer) > 50
        assert response.confidence > 0
        assert 'vlan' in response.answer.lower() or 'VLAN' in response.answer

    def test_routing_basic_query(self, rag_chain):
        """라우팅 기본 쿼리 테스트"""
        response = rag_chain.query("스태틱 라우팅 설정 방법")

        assert isinstance(response, RAGResponse)
        assert response.answer is not None
        assert len(response.answer) > 50
        assert response.confidence > 0
        assert any(keyword in response.answer.lower() for keyword in ['route', 'routing', '라우트', '라우팅'])

    def test_query_with_sources(self, rag_chain):
        """소스 포함 쿼리 테스트"""
        response = rag_chain.query("VLAN 설정", include_sources=True)

        assert len(response.sources) > 0
        assert 'content' in response.sources[0]
        assert 'score' in response.sources[0]

    def test_query_without_sources(self, rag_chain):
        """소스 제외 쿼리 테스트"""
        response = rag_chain.query("VLAN 설정", include_sources=False)

        assert len(response.sources) == 0

    def test_empty_results(self, rag_chain):
        """결과 없음 처리 테스트"""
        response = rag_chain.query("존재하지 않는 기능 xyz123")

        assert response.confidence == 0.0
        assert "찾을 수 없" in response.answer

    def test_confidence_calculation(self, rag_chain):
        """신뢰도 계산 테스트"""
        response = rag_chain.query("VLAN 설정")

        assert 0.0 <= response.confidence <= 1.0

    def test_routing_confidence(self, rag_chain):
        """라우팅 쿼리 신뢰도 테스트"""
        response = rag_chain.query("라우팅 테이블 확인")

        assert 0.0 <= response.confidence <= 1.0
        assert response.confidence > 0.5


class TestHybridSearchRAG:
    """하이브리드 검색 RAG 테스트"""
    
    def test_keyword_extraction(self, mock_vector_store, mock_llm_service):
        """키워드 추출 테스트"""
        rag = HybridSearchRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service,
            keyword_weight=0.3
        )
        
        keywords = rag._extract_cisco_keywords("show vlan brief 명령어로 VLAN 확인")
        
        assert 'show' in keywords or 'vlan' in keywords
    
    def test_hybrid_query(self, mock_vector_store, mock_llm_service):
        """하이브리드 검색 쿼리 테스트"""
        rag = HybridSearchRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        response = rag.query("VLAN 10 설정")
        
        assert response.answer is not None
        assert response.confidence > 0


class TestConversationalRAG:
    """대화형 RAG 테스트"""
    
    def test_conversation_history(self, mock_vector_store, mock_llm_service):
        """대화 히스토리 테스트"""
        rag = ConversationalRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service,
            max_history=5
        )
        
        # 첫 번째 질문
        response1 = rag.query("VLAN 설정 방법")
        assert len(rag.conversation_history) == 1
        
        # 두 번째 질문
        response2 = rag.query("그것의 장점은?")
        assert len(rag.conversation_history) == 2
    
    def test_clear_history(self, mock_vector_store, mock_llm_service):
        """히스토리 초기화 테스트"""
        rag = ConversationalRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        rag.query("VLAN 설정")
        assert len(rag.conversation_history) > 0
        
        rag.clear_history()
        assert len(rag.conversation_history) == 0


class TestStepByStepRAG:
    """단계별 절차 RAG 테스트"""
    
    def test_step_query(self, mock_vector_store, mock_llm_service):
        """단계별 쿼리 테스트"""
        rag = StepByStepRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        response = rag.query("VLAN 설정하는 방법")
        
        assert response.answer is not None
        # 단계 표시 확인
        assert '단계' in response.answer or '1' in response.answer


class TestTroubleshootingRAG:
    """트러블슈팅 RAG 테스트"""

    def test_problem_type_detection(self, mock_vector_store, mock_llm_service):
        """문제 유형 감지 테스트"""
        rag = TroubleshootingRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )

        assert rag._detect_problem_type("인터페이스가 다운됩니다") == 'interface'
        assert rag._detect_problem_type("VLAN 통신이 안됩니다") == 'vlan'
        assert rag._detect_problem_type("라우팅 테이블 문제") == 'routing'

    def test_routing_troubleshooting(self, mock_vector_store, mock_llm_service):
        """라우팅 트러블슈팅 테스트"""
        rag = TroubleshootingRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )

        response = rag.query("라우팅 문제가 발생했습니다")

        assert response.answer is not None
        assert rag._detect_problem_type("라우팅 문제") == 'routing'


class TestRoutingConfiguration:
    """라우팅 설정 관련 RAG 테스트"""

    def test_static_route_query(self, rag_chain):
        """스태틱 라우트 설정 쿼리 테스트"""
        response = rag_chain.query("스태틱 라우트 설정 방법")

        assert isinstance(response, RAGResponse)
        assert response.answer is not None
        assert len(response.answer) > 50
        assert any(keyword in response.answer.lower() for keyword in ['route', 'routing', '라우트', '라우팅'])
        assert response.confidence > 0

    def test_default_route_query(self, rag_chain):
        """디폴트 라우트 설정 쿼리 테스트"""
        response = rag_chain.query("디폴트 라우트 설정")

        assert response.answer is not None
        assert any(keyword in response.answer.lower() for keyword in ['default', '디폴트', '0.0.0.0'])

    def test_ospf_configuration_query(self, rag_chain):
        """OSPF 설정 쿼리 테스트"""
        response = rag_chain.query("OSPF 설정 방법 알려주세요")

        assert response.answer is not None
        assert 'ospf' in response.answer.lower()
        assert response.confidence > 0

    def test_routing_verification_query(self, rag_chain):
        """라우팅 검증 명령어 쿼리 테스트"""
        response = rag_chain.query("라우팅 테이블 확인 명령어")

        assert response.answer is not None
        assert any(keyword in response.answer.lower() for keyword in ['show', 'route', 'routing'])

    def test_routing_query_with_sources(self, rag_chain):
        """라우팅 쿼리 소스 포함 테스트"""
        response = rag_chain.query("스태틱 라우트 설정", include_sources=True)

        assert len(response.sources) > 0
        assert any('route' in source.get('content', '').lower() or 'routing' in source.get('content', '').lower()
                   for source in response.sources)
        assert all('score' in source for source in response.sources)
        assert all(source['score'] > 0 for source in response.sources)

    def test_routing_step_by_step(self, mock_vector_store, mock_llm_service):
        """라우팅 설정 단계별 안내 테스트"""
        rag = StepByStepRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )

        response = rag.query("스태틱 라우트를 설정하는 방법")

        assert response.answer is not None
        assert '단계' in response.answer or '1' in response.answer
        assert any(keyword in response.answer.lower() for keyword in ['route', 'routing'])

    def test_routing_hybrid_search(self, mock_vector_store, mock_llm_service):
        """라우팅 하이브리드 검색 테스트"""
        rag = HybridSearchRAG(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service,
            keyword_weight=0.3
        )

        response = rag.query("ip route 명령어로 경로 설정")

        assert response.answer is not None
        assert response.confidence > 0


class TestRAGFactory:
    """RAG 팩토리 테스트"""

    def test_mode_selection(self, mock_vector_store, mock_llm_service):
        """모드 선택 테스트"""
        factory = RAGFactory(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        # 각 모드별 체인 생성
        default_chain = factory.get_chain(RAGMode.DEFAULT)
        hybrid_chain = factory.get_chain(RAGMode.HYBRID)
        
        assert isinstance(default_chain, CiscoRAGChain)
        assert isinstance(hybrid_chain, HybridSearchRAG)
    
    def test_auto_mode_selection(self, mock_vector_store, mock_llm_service):
        """자동 모드 선택 테스트"""
        factory = RAGFactory(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        assert factory.auto_select_mode("연결이 안됩니다") == RAGMode.TROUBLESHOOTING
        assert factory.auto_select_mode("설정 방법을 알려주세요") == RAGMode.STEP_BY_STEP
        assert factory.auto_select_mode("STP와 RSTP 비교") == RAGMode.COMPARISON


class TestUnifiedInterface:
    """통합 인터페이스 테스트"""
    
    def test_unified_query(self, mock_vector_store, mock_llm_service):
        """통합 쿼리 테스트"""
        interface = UnifiedRAGInterface(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        response = interface.query("VLAN 설정", auto_mode=True)
        
        assert response.answer is not None
    
    def test_conversation_session(self, mock_vector_store, mock_llm_service):
        """대화 세션 테스트"""
        interface = UnifiedRAGInterface(
            vector_store=mock_vector_store,
            llm_service=mock_llm_service
        )
        
        session_id = "test_session_1"
        
        response1 = interface.conversation("VLAN 설정", session_id)
        response2 = interface.conversation("그 다음은?", session_id)
        
        assert response1 is not None
        assert response2 is not None
        
        interface.delete_session(session_id)
        assert session_id not in interface._conversation_sessions


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])