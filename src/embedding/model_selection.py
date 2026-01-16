# src/embedding/model_selection.py

"""
시스코 네트워크 매뉴얼을 위한 임베딩 모델 선정 가이드

평가 기준:
1. 영문 기술 문서 성능 - 영어 IT/네트워크 용어 이해
2. 한국어 성능 - 한글 기술 문서 처리 능력 (번역된 질문용)
3. 기술 도메인 적합성 - 네트워크/시스템 지식
4. 긴 컨텍스트 처리 - 설정 가이드 등 긴 문서
5. 검색 정확도 - 유사 문서 검색 성능
6. 추론 속도 - 실시간 처리 가능 여부

중요: 시스코 매뉴얼은 영문이므로 영문 성능이 최우선
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum


class ModelCategory(Enum):
    ENGLISH_TECHNICAL = "english_technical"  # 영문 기술 문서 특화
    MULTILINGUAL = "multilingual"  # 다국어 지원
    KOREAN_SPECIFIC = "korean_specific"  # 한국어 특화
    ENGLISH_DOMINANT = "english_dominant"  # 영어 중심


@dataclass
class EmbeddingModelInfo:
    name: str
    model_id: str
    dimension: int
    max_tokens: int
    category: ModelCategory
    english_score: float  # 1-10 (영어 성능)
    korean_score: float  # 1-10 (한국어 성능)
    tech_domain_score: float  # 1-10 (기술 문서 이해도)
    speed_score: float  # 1-10 (추론 속도)
    memory_gb: float
    notes: str
    use_case: str = "general"  # general, document, query


# ============================================================================
# 영문 기술 문서용 임베딩 모델 (시스코 매뉴얼 임베딩용)
# ============================================================================
ENGLISH_DOCUMENT_MODELS = [
    # 1순위: 영문 기술 문서 최고 성능
    EmbeddingModelInfo(
        name="BGE-Large-EN-v1.5",
        model_id="BAAI/bge-large-en-v1.5",
        dimension=1024,
        max_tokens=512,
        category=ModelCategory.ENGLISH_TECHNICAL,
        english_score=9.8,
        korean_score=3.0,
        tech_domain_score=9.5,
        speed_score=7.5,
        memory_gb=1.3,
        notes="영문 기술 문서 최적화. MTEB 벤치마크 1위권. Retrieval 성능 탁월",
        use_case="document"
    ),

    # 2순위: 긴 컨텍스트 + 영문 우수
    EmbeddingModelInfo(
        name="E5-Large-v2",
        model_id="intfloat/e5-large-v2",
        dimension=1024,
        max_tokens=512,
        category=ModelCategory.ENGLISH_TECHNICAL,
        english_score=9.5,
        korean_score=3.5,
        tech_domain_score=9.0,
        speed_score=8.0,
        memory_gb=1.3,
        notes="영어 성능 우수. 프리픽스(query:/passage:) 사용. 안정적",
        use_case="document"
    ),

    # 3순위: 균형잡힌 영문 모델
    EmbeddingModelInfo(
        name="BGE-Base-EN-v1.5",
        model_id="BAAI/bge-base-en-v1.5",
        dimension=768,
        max_tokens=512,
        category=ModelCategory.ENGLISH_TECHNICAL,
        english_score=9.3,
        korean_score=3.0,
        tech_domain_score=9.0,
        speed_score=9.0,
        memory_gb=0.4,
        notes="영문 성능 우수하면서 빠름. 리소스 효율적",
        use_case="document"
    ),

    # 4순위: 초경량 영문 모델
    EmbeddingModelInfo(
        name="All-MiniLM-L6-v2",
        model_id="sentence-transformers/all-MiniLM-L6-v2",
        dimension=384,
        max_tokens=256,
        category=ModelCategory.ENGLISH_TECHNICAL,
        english_score=8.5,
        korean_score=2.0,
        tech_domain_score=8.0,
        speed_score=10.0,
        memory_gb=0.08,
        notes="초경량 초고속. 메모리 제약 환경용",
        use_case="document"
    ),
]

# ============================================================================
# 한국어 쿼리용 임베딩 모델 (번역된 질문 임베딩용)
# ============================================================================
KOREAN_QUERY_MODELS = [
    # 1순위: 한국어 검색 최적화
    EmbeddingModelInfo(
        name="KR-SBERT-Medium",
        model_id="snunlp/KR-SBERT-V40K-klueNLI-augSTS",
        dimension=768,
        max_tokens=512,
        category=ModelCategory.KOREAN_SPECIFIC,
        english_score=4.0,
        korean_score=9.5,
        tech_domain_score=7.5,
        speed_score=9.0,
        memory_gb=0.4,
        notes="한국어 쿼리 최적화. 빠르고 정확",
        use_case="query"
    ),

    # 2순위: 한국어 문장 임베딩
    EmbeddingModelInfo(
        name="Ko-Sentence-BERT",
        model_id="jhgan/ko-sbert-nli",
        dimension=768,
        max_tokens=512,
        category=ModelCategory.KOREAN_SPECIFIC,
        english_score=3.5,
        korean_score=9.0,
        tech_domain_score=7.0,
        speed_score=9.5,
        memory_gb=0.4,
        notes="한국어 문장 유사도 특화",
        use_case="query"
    ),
]

# ============================================================================
# 다국어 모델 (영어 문서 + 한국어 쿼리 통합)
# ============================================================================
MULTILINGUAL_MODELS = [
    # 1순위: 다국어 고성능
    EmbeddingModelInfo(
        name="BGE-M3",
        model_id="BAAI/bge-m3",
        dimension=1024,
        max_tokens=8192,
        category=ModelCategory.MULTILINGUAL,
        english_score=9.0,
        korean_score=8.5,
        tech_domain_score=8.5,
        speed_score=7.0,
        memory_gb=2.2,
        notes="다국어 지원. Dense+Sparse+ColBERT. 긴 컨텍스트",
        use_case="general"
    ),

    # 2순위: 다국어 균형
    EmbeddingModelInfo(
        name="Multilingual-E5-Large",
        model_id="intfloat/multilingual-e5-large",
        dimension=1024,
        max_tokens=512,
        category=ModelCategory.MULTILINGUAL,
        english_score=8.8,
        korean_score=8.0,
        tech_domain_score=8.0,
        speed_score=7.5,
        memory_gb=2.2,
        notes="안정적 다국어 성능. 프로덕션 검증",
        use_case="general"
    ),
]

# 통합 모델 리스트
RECOMMENDED_MODELS = ENGLISH_DOCUMENT_MODELS + KOREAN_QUERY_MODELS + MULTILINGUAL_MODELS


def select_document_model(
    max_memory_gb: float = 4.0,
    need_long_context: bool = False,
    prefer_speed: bool = False
) -> EmbeddingModelInfo:
    """
    영문 문서 임베딩 모델 선택 (시스코 매뉴얼용)

    Args:
        max_memory_gb: 최대 메모리
        need_long_context: 긴 컨텍스트 필요 여부
        prefer_speed: 속도 우선 여부

    Returns:
        최적 모델
    """
    candidates = [m for m in ENGLISH_DOCUMENT_MODELS if m.memory_gb <= max_memory_gb]

    if not candidates:
        candidates = ENGLISH_DOCUMENT_MODELS

    if prefer_speed:
        candidates.sort(key=lambda x: x.speed_score, reverse=True)
    else:
        # 영문 성능 + 기술 도메인 점수 기준
        candidates.sort(
            key=lambda x: (x.english_score * 0.6 + x.tech_domain_score * 0.4),
            reverse=True
        )

    return candidates[0]


def select_query_model(
    language: str = "ko",
    max_memory_gb: float = 4.0
) -> EmbeddingModelInfo:
    """
    쿼리 임베딩 모델 선택

    Args:
        language: 쿼리 언어 ('ko', 'en')
        max_memory_gb: 최대 메모리

    Returns:
        최적 모델
    """
    if language == "ko":
        candidates = [m for m in KOREAN_QUERY_MODELS if m.memory_gb <= max_memory_gb]
        if candidates:
            candidates.sort(key=lambda x: x.korean_score, reverse=True)
            return candidates[0]

    # 영어 쿼리는 문서 모델 사용
    return select_document_model(max_memory_gb=max_memory_gb)


def select_unified_model(
    max_memory_gb: float = 4.0,
    need_long_context: bool = False
) -> EmbeddingModelInfo:
    """
    통합 모델 선택 (문서 + 쿼리 동일 모델)

    영어 문서 + 한국어 쿼리를 하나의 모델로 처리

    Args:
        max_memory_gb: 최대 메모리
        need_long_context: 긴 컨텍스트 필요 여부

    Returns:
        최적 다국어 모델
    """
    candidates = [m for m in MULTILINGUAL_MODELS if m.memory_gb <= max_memory_gb]

    if need_long_context:
        candidates = [m for m in candidates if m.max_tokens >= 1024]

    if candidates:
        # 영문 + 한국어 + 기술 점수 종합
        candidates.sort(
            key=lambda x: (x.english_score * 0.5 + x.korean_score * 0.3 + x.tech_domain_score * 0.2),
            reverse=True
        )
        return candidates[0]

    return MULTILINGUAL_MODELS[0]


# 최종 권장 전략
FINAL_RECOMMENDATION = """
시스코 영문 매뉴얼 + 한국어 질의응답을 위한 최종 권장:

═══════════════════════════════════════════════════════════════
전략 1: 분리 임베딩 (최고 성능) ⭐ 권장
═══════════════════════════════════════════════════════════════

▶ 영문 문서 임베딩 (시스코 매뉴얼):
  1순위: BAAI/bge-large-en-v1.5
     - 영문 기술 문서 최적화
     - MTEB 벤치마크 최상위
     - 네트워크 용어 이해도 탁월

  2순위: intfloat/e5-large-v2
     - 영어 성능 우수
     - 안정적 retrieval 성능

▶ 한국어 쿼리 임베딩 (번역된 질문):
  - 번역 후 영문 모델로 임베딩 (BGE-Large-EN 사용)

장점: 최고 성능, 각 언어에 최적화
단점: 모델 2개 로딩 (메모리 약 2.6GB)

═══════════════════════════════════════════════════════════════
전략 2: 통합 임베딩 (균형)
═══════════════════════════════════════════════════════════════

▶ 다국어 모델 (문서 + 쿼리 통합):
  1순위: BAAI/bge-m3
     - 영어(9.0) + 한국어(8.5) 모두 우수
     - 8192 토큰 지원
     - Dense + Sparse 하이브리드

  2순위: intfloat/multilingual-e5-large
     - 안정적 다국어 성능
     - 프로덕션 검증

장점: 모델 1개, 메모리 절약
단점: 영문 전용 모델보다 약간 낮은 성능

═══════════════════════════════════════════════════════════════
전략 3: 경량 임베딩 (리소스 제약)
═══════════════════════════════════════════════════════════════

▶ 경량 영문 모델:
  - BAAI/bge-base-en-v1.5 (0.4GB)
  - sentence-transformers/all-MiniLM-L6-v2 (0.08GB)

장점: 빠름, 메모리 적음
단점: 성능 다소 낮음

═══════════════════════════════════════════════════════════════
결론
═══════════════════════════════════════════════════════════════

시스코 영문 매뉴얼 환경:
✓ 최고 성능 우선 → 전략 1 (BGE-Large-EN-v1.5)
✓ 균형 (메모리/성능) → 전략 2 (BGE-M3)
✓ 리소스 제약 → 전략 3 (BGE-Base-EN-v1.5)

핵심: 영문 매뉴얼이므로 영문 모델이 다국어 모델보다 성능 우수!
"""