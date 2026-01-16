# src/embedding/benchmark.py

"""
시스코 매뉴얼 검색 시나리오 기반 임베딩 모델 벤치마크
"""

from typing import List, Dict, Tuple
import time
import numpy as np
from embedding_service import CiscoEmbeddingService


# 테스트 쿼리 및 관련 문서
TEST_CASES = [
    {
        "query": "VLAN 설정 방법",
        "relevant_docs": [
            "VLAN을 생성하려면 vlan 명령어를 사용합니다. Switch(config)# vlan 10",
            "VLAN(Virtual LAN)은 논리적 네트워크 분할 기술입니다.",
        ],
        "irrelevant_docs": [
            "OSPF 라우팅 프로토콜 설정 가이드",
            "스위치 하드웨어 사양 및 설치 방법",
        ]
    },
    {
        "query": "show interface status 명령어",
        "relevant_docs": [
            "Switch# show interface status 명령어로 포트 상태를 확인합니다.",
            "인터페이스 상태 확인: show interface status, show interface brief",
        ],
        "irrelevant_docs": [
            "IP 라우팅 테이블 조회 방법",
            "SNMP 커뮤니티 설정",
        ]
    },
    {
        "query": "트렁크 포트 설정",
        "relevant_docs": [
            "트렁크 모드 설정: switchport mode trunk 명령 사용",
            "802.1Q 트렁킹을 통해 여러 VLAN 트래픽을 전송합니다.",
        ],
        "irrelevant_docs": [
            "액세스 포트 보안 설정",
            "스패닝 트리 프로토콜 개요",
        ]
    },
]


def run_benchmark(model_names: List[str]) -> Dict:
    """
    여러 모델 벤치마크 실행
    """
    results = {}
    
    for model_name in model_names:
        print(f"\n{'='*60}")
        print(f"Testing: {model_name}")
        print('='*60)
        
        try:
            service = CiscoEmbeddingService(
                model_name=model_name,
                use_prefix='e5' in model_name.lower()
            )
            
            metrics = evaluate_model(service)
            results[model_name] = metrics
            
            print(f"\nResults for {model_name}:")
            print(f"  MRR: {metrics['mrr']:.4f}")
            print(f"  Hit@1: {metrics['hit_at_1']:.4f}")
            print(f"  Hit@3: {metrics['hit_at_3']:.4f}")
            print(f"  Avg Latency: {metrics['avg_latency_ms']:.2f}ms")
            
        except Exception as e:
            print(f"Error testing {model_name}: {e}")
            results[model_name] = {'error': str(e)}
    
    return results


def evaluate_model(service: CiscoEmbeddingService) -> Dict:
    """
    단일 모델 평가
    """
    mrr_scores = []
    hit_at_1 = []
    hit_at_3 = []
    latencies = []
    
    for case in TEST_CASES:
        query = case['query']
        all_docs = case['relevant_docs'] + case['irrelevant_docs']
        relevant_indices = set(range(len(case['relevant_docs'])))
        
        # 문서 임베딩
        from langchain_core.documents import Document
        docs = [Document(page_content=d, metadata={}) for d in all_docs]
        doc_results = service.embed_documents(docs, show_progress=False)
        doc_embeddings = np.array([r['embedding'] for r in doc_results])
        
        # 쿼리 임베딩 및 검색 (시간 측정)
        start_time = time.time()
        query_embedding = service.embed_query(query)
        similarities = service.compute_similarity(query_embedding, doc_embeddings)
        latency = (time.time() - start_time) * 1000
        latencies.append(latency)
        
        # 순위 계산
        ranked_indices = np.argsort(similarities)[::-1]
        
        # MRR 계산
        for rank, idx in enumerate(ranked_indices, 1):
            if idx in relevant_indices:
                mrr_scores.append(1.0 / rank)
                break
        else:
            mrr_scores.append(0.0)
        
        # Hit@K 계산
        top_1 = set(ranked_indices[:1])
        top_3 = set(ranked_indices[:3])
        
        hit_at_1.append(1.0 if top_1 & relevant_indices else 0.0)
        hit_at_3.append(1.0 if top_3 & relevant_indices else 0.0)
    
    return {
        'mrr': np.mean(mrr_scores),
        'hit_at_1': np.mean(hit_at_1),
        'hit_at_3': np.mean(hit_at_3),
        'avg_latency_ms': np.mean(latencies),
        'dimension': service.dimension
    }


if __name__ == "__main__":
    models_to_test = [
        "BAAI/bge-m3",
        "intfloat/multilingual-e5-large",
        "intfloat/multilingual-e5-base",
        "jhgan/ko-sbert-nli",
    ]
    
    results = run_benchmark(models_to_test)
    
    print("\n" + "="*60)
    print("FINAL RANKING")
    print("="*60)
    
    # MRR 기준 정렬
    sorted_results = sorted(
        [(k, v) for k, v in results.items() if 'mrr' in v],
        key=lambda x: x[1]['mrr'],
        reverse=True
    )
    
    for rank, (model, metrics) in enumerate(sorted_results, 1):
        print(f"{rank}. {model}")
        print(f"   MRR: {metrics['mrr']:.4f}, Hit@1: {metrics['hit_at_1']:.4f}")