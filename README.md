# RAGParser - 시스코 매뉴얼 RAG 시스템

시스코 네트워크 장비 매뉴얼을 위한 RAG (Retrieval-Augmented Generation) 시스템입니다.

## 주요 기능

### 1. PDF 파싱 및 전처리
- 시스코 매뉴얼 PDF 파싱
- CLI 명령어 자동 감지 및 추출
- 마크다운 변환

### 2. 벡터 스토어
- ChromaDB 기반 벡터 데이터베이스
- 시맨틱 검색
- 메타데이터 필터링

### 3. RAG 체인
- 기본 RAG 체인
- 하이브리드 검색 (벡터 + 키워드)
- Re-Ranking
- 대화형 RAG
- 단계별 절차 생성
- 트러블슈팅 특화

### 4. **다국어 지원** ⭐ NEW
- **한국어 질문 → 영문 매뉴얼 검색 → 한국어 답변**
- 자동 언어 감지
- 기술 용어 및 CLI 명령어 보존
- 여러 번역 엔진 지원 (Google, DeepL, LLM)

### 5. **이중 임베딩 전략** ⭐ NEW
- **영문 문서 전용 모델 + 한국어 쿼리 번역**
- 영문 기술 문서 최적화 (MTEB 최상위 모델)
- 다국어 모델 대비 5-10% 성능 향상
- 유연한 전략 선택 (이중/통합/경량)

## 설치

```bash
# 기본 설치
pip install -r requirements.txt

# 번역 기능 사용 시
pip install googletrans==4.0.0rc1

# 고품질 번역 (DeepL) 사용 시
pip install deepl
```

## 빠른 시작

### 1. 기본 RAG 사용

```python
from src.vectorstore.chroma_store import CiscoVectorStore
from src.llm.llama_service import OllamaService
from src.rag.rag_chain import CiscoRAGChain

# 벡터 스토어 초기화
vector_store = CiscoVectorStore(
    collection_name="cisco_manuals",
    persist_directory="./data/chroma_db"
)

# LLM 서비스 초기화
llm_service = OllamaService(model_name="llama3.1:8b")

# RAG 체인 생성
rag = CiscoRAGChain(vector_store=vector_store, llm_service=llm_service)

# 질문
response = rag.query("How to configure VLAN?")
print(response.answer)
```

### 2. 다국어 RAG 사용 (한국어 ⟷ 영어)

```python
from src.rag.multilingual_rag import create_multilingual_rag

# 다국어 RAG 체인 생성
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="google"  # 또는 "deepl", "llm"
)

# 한국어로 질문 → 자동으로 영어로 번역 → 영문 매뉴얼 검색 → 한국어로 답변
response = rag.query("VLAN을 설정하는 방법을 알려주세요")
print(response.answer)  # 한국어 답변
```

### 3. 오프라인 환경에서 사용 ⭐ 자동 감지

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# 먼저 온라인 환경에서 모델 다운로드
# python scripts/download_models.py

# 오프라인 환경에서는 자동으로 감지!
# local_files_only를 지정하지 않아도 됨
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
    # 네트워크 연결 상태에 따라 자동으로 오프라인 모드 활성화
)

# 또는 명시적으로 오프라인 모드 지정
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=True  # 명시적 오프라인 모드
)

# 또는 로컬 경로 직접 지정
service = CiscoEmbeddingService(
    model_name="./models/BAAI_bge-m3"
)
```

## 문서

- **[임베딩 전략 가이드](EMBEDDING_STRATEGY_GUIDE.md)** ⭐ - 영문 문서 최적 임베딩 전략
- **[오프라인 사용 가이드](docs/OFFLINE_USAGE.md)** ⭐ - 네트워크 없이 모델 사용하기
- **[오프라인 자동 감지](docs/OFFLINE_AUTO_DETECT.md)** 🆕 - 네트워크 상태 자동 감지 기능
- [다국어 RAG 가이드](MULTILINGUAL_RAG_GUIDE.md) - 번역 기능 상세 설명
- [설정 가이드](SETUP_COMPLETE.md) - 전체 설정 가이드
- [임베딩 모델 선정](src/embedding/model_selection.py) - 모델 선택 가이드

## 프로젝트 구조

```
RAGParser/
├── src/
│   ├── parser/              # PDF 파싱
│   ├── splitter/            # 텍스트 분할
│   ├── embedding/           # 임베딩 모델
│   │   ├── model_selection.py           # 모델 선택 (영문/다국어)
│   │   ├── embedding_service.py         # 기본 임베딩
│   │   └── dual_embedding_service.py    # 이중 임베딩 ⭐
│   ├── vectorstore/         # 벡터 데이터베이스
│   ├── llm/                 # LLM 서비스
│   ├── rag/                 # RAG 체인
│   │   ├── rag_chain.py          # 기본 RAG
│   │   ├── advanced_rag.py       # 고급 RAG
│   │   └── multilingual_rag.py   # 다국어 RAG ⭐
│   └── translation/         # 번역 서비스 ⭐
├── examples/                # 사용 예제
│   ├── multilingual_rag_example.py
│   └── dual_embedding_example.py  ⭐
├── tests/                   # 테스트
│   └── test_translation.py
├── data/                    # 데이터
├── processed/               # 처리된 문서
└── requirements.txt         # 의존성
```

## 주요 기능 상세

### 다국어 RAG (Multilingual RAG)

시스코 매뉴얼이 영문으로 작성되어 있어도 한국어로 질의응답할 수 있습니다.

**작동 원리:**
```
한국어 질문 → 영어 번역 → 영문 매뉴얼 검색 → 영어 답변 생성 → 한국어 번역 → 한국어 답변
```

**지원 번역 엔진:**
- **Google Translate**: 무료, API 키 불필요, 빠른 속도
- **DeepL**: 고품질, 월 500,000자 무료
- **LLM 번역**: 완전 오프라인, 외부 API 불필요

**특징:**
- 자동 언어 감지
- CLI 명령어와 기술 용어 원어 보존
- 이중 언어 모드 (한국어 + 영어 답변 동시 제공)
- 스트리밍 지원

자세한 내용은 [다국어 RAG 가이드](MULTILINGUAL_RAG_GUIDE.md)를 참조하세요.

### 고급 RAG 기능

1. **하이브리드 검색**: 벡터 검색 + 키워드 매칭
2. **Re-Ranking**: LLM 기반 문서 재순위화
3. **대화형 RAG**: 이전 대화 컨텍스트 유지
4. **단계별 절차 생성**: 설정 가이드 자동 생성
5. **트러블슈팅**: 문제 진단 및 해결 방법 제시

## 예제

### 예제 1: 한국어로 CLI 명령어 검색

```python
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="google"
)

# CLI 명령어 검색
response = rag.query_cli_command("MAC 주소 테이블 확인")
print(response.answer)
```

### 예제 2: 이중 언어 모드

```python
# 이중 언어 모드로 생성
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="google",
    bilingual=True  # 한국어 + 영어 답변
)

responses = rag.query("스위치 포트를 trunk 모드로 설정하는 방법은?")

print("한국어:", responses['korean'].answer)
print("영어:", responses['english'].answer)
```

### 예제 3: 트러블슈팅

```python
from src.rag.advanced_rag import TroubleshootingRAG

troubleshoot_rag = TroubleshootingRAG(
    vector_store=vector_store,
    llm_service=llm_service
)

response = troubleshoot_rag.query("포트가 err-disabled 상태입니다")
print(response.answer)
```

## 테스트

```bash
# 번역 기능 테스트
pytest tests/test_translation.py -v

# 전체 예제 실행
python examples/multilingual_rag_example.py
```

## 성능 최적화

### 임베딩 전략

**영문 매뉴얼 환경 (권장):**
- **문서 임베딩**: BGE-Large-EN-v1.5 (영문 전용, MTEB 최상위)
- **쿼리 임베딩**: 번역 후 동일 모델 사용
- **성능**: 다국어 모델 대비 5-10% 향상

**다국어 환경:**
- **통합 모델**: BGE-M3 (다국어 지원, 8192 토큰)
- **특징**: 번역 불필요, 간편한 구조

**경량 환경:**
- **모델**: All-MiniLM-L6-v2 (0.08GB)
- **특징**: 초고속, 메모리 효율

자세한 내용: [임베딩 전략 가이드](EMBEDDING_STRATEGY_GUIDE.md)

### 기타 구성

- **LLM**: Llama 3.1 8B (Ollama)
- **벡터 DB**: ChromaDB (빠른 검색)
- **번역**: Google Translate (빠름) 또는 DeepL (고품질)

## 시스템 요구사항

- Python 3.8+
- 8GB RAM 이상
- GPU (선택, LLM 가속용)
- Ollama (LLM 서비스)

## 라이선스

MIT License

## 기여

Pull Request와 Issue는 언제나 환영합니다!

## 문의

문제가 있으면 Issue를 생성해주세요.
