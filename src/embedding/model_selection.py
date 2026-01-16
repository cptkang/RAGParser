# src/embedding/model_selection.py

"""
시스코 네트워크 매뉴얼을 위한 임베딩 모델 선정 가이드

평가 기준:
1. 한국어 성능 - 한글 기술 문서 처리 능력
2. 기술 도메인 적합성 - IT/네트워크 용어 이해
3. 긴 컨텍스트 처리 - 설정 가이드 등 긴 문서
4. 검색 정확도 - 유사 문서 검색 성능
5. 추론 속도 - 실시간 처리 가능 여부
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum


class ModelCategory(Enum):
    MULTILINGUAL = "multilingual"
    KOREAN_SPECIFIC = "korean_specific"
    ENGLISH_DOMINANT = "english_dominant"


@dataclass
class EmbeddingModelInfo:
    name: str
    model_id: str
    dimension: int
    max_tokens: int
    category: ModelCategory
    korean_score: float  # 1-10
    tech_domain_score: float  # 1-10
    speed_score: float  # 1-10
    memory_gb: float
    notes: str


# 추천 모델 목록
RECOMMENDED_MODELS = [
    # 1순위: 다국어 고성능 모델
    EmbeddingModelInfo(
        name="BGE-M3",
        model_id="BAAI/bge-m3",
        dimension=1024,
        max_tokens=8192,
        category=ModelCategory.MULTILINGUAL,
        korean_score=9.0,
        tech_domain_score=8.5,
        speed_score=7.0,
        memory_gb=2.2,
        notes="최신 다국어 모델. Dense + Sparse + ColBERT 지원. 긴 컨텍스트에 우수"
    ),
    
    # 2순위: 균형 잡힌 다국어 모델
    EmbeddingModelInfo(
        name="Multilingual-E5-Large",
        model_id="intfloat/multilingual-e5-large",
        dimension=1024,
        max_tokens=512,
        category=ModelCategory.MULTILINGUAL,
        korean_score=8.5,
        tech_domain_score=8.0,
        speed_score=7.5,
        memory_gb=2.2,
        notes="안정적인 다국어 성능. 프로덕션 검증됨"
    ),
    
    # 3순위: 한국어 특화 모델
    EmbeddingModelInfo(
        name="KR-SBERT",
        model_id="snunlp/KR-SBERT-V40K-klueNLI-augSTS",
        dimension=768,
        max_tokens=512,
        category=ModelCategory.KOREAN_SPECIFIC,
        korean_score=9.5,
        tech_domain_score=7.0,
        speed_score=8.5,
        memory_gb=0.4,
        notes="한국어 최적화. 경량. 기술 용어 일부 미지원 가능"
    ),
    
    # 4순위: 경량 다국어 모델
    EmbeddingModelInfo(
        name="Multilingual-E5-Base",
        model_id="intfloat/multilingual-e5-base",
        dimension=768,
        max_tokens=512,
        category=ModelCategory.MULTILINGUAL,
        korean_score=8.0,
        tech_domain_score=7.5,
        speed_score=9.0,
        memory_gb=1.1,
        notes="리소스 제약 환경에 적합. 성능과 속도 균형"
    ),
    
    # 5순위: 최신 한국어 모델
    EmbeddingModelInfo(
        name="Ko-Sentence-BERT",
        model_id="jhgan/ko-sbert-nli",
        dimension=768,
        max_tokens=512,
        category=ModelCategory.KOREAN_SPECIFIC,
        korean_score=9.0,
        tech_domain_score=6.5,
        speed_score=9.0,
        memory_gb=0.4,
        notes="한국어 문장 임베딩 특화. 기술 문서 fine-tuning 권장"
    ),
]


def select_model(
    korean_priority: bool = True,
    max_memory_gb: float = 4.0,
    need_long_context: bool = True
) -> EmbeddingModelInfo:
    """
    요구사항에 맞는 모델 선택
    
    시스코 한국어 매뉴얼 권장: BGE-M3 또는 Multilingual-E5-Large
    """
    candidates = [m for m in RECOMMENDED_MODELS if m.memory_gb <= max_memory_gb]
    
    if need_long_context:
        candidates = [m for m in candidates if m.max_tokens >= 1024]
    
    if korean_priority:
        candidates.sort(key=lambda x: x.korean_score, reverse=True)
    else:
        candidates.sort(
            key=lambda x: (x.tech_domain_score + x.korean_score) / 2, 
            reverse=True
        )
    
    return candidates[0] if candidates else RECOMMENDED_MODELS[0]


# 최종 권장 모델
FINAL_RECOMMENDATION = """
시스코 네트워크 장비 한국어 매뉴얼을 위한 최종 권장:

1순위: BAAI/bge-m3
   - 한국어 + 영어 기술 용어 모두 우수
   - 8192 토큰으로 긴 설정 가이드 처리 가능
   - Dense + Sparse 하이브리드 검색 지원
   
2순위: intfloat/multilingual-e5-large  
   - 안정적인 프로덕션 성능
   - 다양한 환경에서 검증됨
   
한국어 순수 문서(번역본)만 있는 경우:
   - snunlp/KR-SBERT-V40K-klueNLI-augSTS 고려
   - 단, CLI 명령어(영어)와 함께 사용 시 다국어 모델 권장
"""