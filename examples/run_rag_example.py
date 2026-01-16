# examples/run_rag_example.py

"""
시스코 매뉴얼 RAG 시스템 실행 예제
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.vectorstore.chroma_store import CiscoVectorStore
from src.embedding.embedding_service import CiscoEmbeddingService
from src.llm.llama_service import OllamaService
from src.rag.rag_factory import UnifiedRAGInterface, RAGMode


def main():
    print("=" * 60)
    print("시스코 매뉴얼 RAG 시스템")
    print("=" * 60)
    
    # 1. 서비스 초기화
    print("\n[1] 서비스 초기화 중...")
    
    embedding_service = CiscoEmbeddingService(
        model_name="BAAI/bge-m3"
    )
    
    vector_store = CiscoVectorStore(
        persist_directory="./vectordb",
        embedding_service=embedding_service
    )
    
    llm_service = OllamaService(
        model_name="llama3.1:8b"
    )
    
    # 2. 통합 인터페이스 생성
    rag = UnifiedRAGInterface(
        vector_store=vector_store,
        llm_service=llm_service
    )
    
    print("초기화 완료!")
    
    # 3. 다양한 쿼리 예제
    examples = [
        {
            "mode": "default",
            "question": "VLAN 10을 생성하는 방법을 알려주세요"
        },
        {
            "mode": "stepbystep",
            "question": "트렁크 포트 설정 절차"
        },
        {
            "mode": "troubleshooting",
            "question": "인터페이스가 down 상태인데 원인이 뭔가요?"
        },
        {
            "mode": "hybrid",
            "question": "show vlan brief 명령어 설명"
        }
    ]
    
    for example in examples:
        print(f"\n{'='*60}")
        print(f"모드: {example['mode']}")
        print(f"질문: {example['question']}")
        print("-" * 60)
        
        response = rag.query(
            question=example['question'],
            mode=example['mode']
        )
        
        print(f"\n답변:\n{response.answer}")
        print(f"\n신뢰도: {response.confidence:.2%}")
        print(f"참조 문서 수: {len(response.sources)}")
    
    # 4. 대화형 세션 예제
    print(f"\n{'='*60}")
    print("대화형 세션 예제")
    print("-" * 60)
    
    session_id = "demo_session"
    
    conversation_flow = [
        "VLAN이 뭔가요?",
        "그럼 VLAN을 만들려면 어떻게 해요?",
        "포트에 할당하는 방법은요?"
    ]
    
    for question in conversation_flow:
        print(f"\n사용자: {question}")
        response = rag.conversation(question, session_id)
        print(f"\n어시스턴트: {response.answer[:300]}...")
    
    # 세션 정리
    rag.delete_session(session_id)
    
    # 5. 비교 예제
    print(f"\n{'='*60}")
    print("비교 분석 예제")
    print("-" * 60)
    
    comparison_response = rag.compare(
        item1="STP",
        item2="RSTP",
        aspect="수렴 시간"
    )
    
    print(f"\nSTP vs RSTP 비교:\n{comparison_response.answer}")
    
    print("\n" + "=" * 60)
    print("예제 실행 완료!")


if __name__ == "__main__":
    main()