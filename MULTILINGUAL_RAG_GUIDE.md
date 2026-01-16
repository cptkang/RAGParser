# 다국어 RAG 가이드

시스코 매뉴얼이 영문으로 작성되어 있어도 한국어로 질의응답할 수 있는 다국어 RAG 시스템입니다.

## 목차
1. [개요](#개요)
2. [설치](#설치)
3. [사용 방법](#사용-방법)
4. [번역기 종류](#번역기-종류)
5. [예제](#예제)
6. [FAQ](#faq)

## 개요

### 작동 원리

```
한국어 질문 → 영어 번역 → 영문 매뉴얼 검색 → 영어 답변 생성 → 한국어 번역 → 한국어 답변
```

### 주요 특징

- **자동 언어 감지**: 입력 언어를 자동으로 감지
- **기술 용어 보존**: CLI 명령어와 기술 용어는 원어 그대로 유지
- **다양한 번역 엔진**: Google Translate, DeepL, LLM 번역 지원
- **이중 언어 모드**: 한국어와 영어 답변 동시 제공
- **스트리밍 지원**: 실시간 답변 생성

## 설치

### 1. 필수 패키지 설치

```bash
# 기본 패키지 (Google Translate 사용)
pip install googletrans==4.0.0rc1

# 또는 고품질 번역이 필요한 경우 (DeepL)
pip install deepl
```

### 2. 환경 변수 설정 (DeepL 사용 시)

```bash
# .env 파일에 추가
DEEPL_API_KEY=your_deepl_api_key_here
```

### 3. 전체 의존성 설치

```bash
pip install -r requirements.txt
```

## 사용 방법

### 기본 사용법

```python
from src.vectorstore.chroma_store import CiscoVectorStore
from src.llm.llama_service import OllamaService
from src.rag.multilingual_rag import create_multilingual_rag

# 1. 벡터 스토어 초기화
vector_store = CiscoVectorStore(
    collection_name="cisco_manuals",
    persist_directory="./data/chroma_db"
)

# 2. LLM 서비스 초기화
llm_service = OllamaService(model_name="llama3.1:8b")

# 3. 다국어 RAG 생성
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="google"  # 또는 "deepl", "llm"
)

# 4. 한국어로 질문
response = rag.query("VLAN을 설정하는 방법을 알려주세요")
print(response.answer)
```

### 이중 언어 모드

한국어와 영어 답변을 모두 받을 수 있습니다.

```python
# 이중 언어 모드 활성화
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="google",
    bilingual=True  # 이중 언어 모드
)

# 쿼리 실행
responses = rag.query("스위치 포트를 trunk 모드로 설정하는 방법은?")

# 한국어 답변
print("한국어:")
print(responses['korean'].answer)

# 영어 답변
print("\n영어:")
print(responses['english'].answer)
```

### 스트리밍 응답

```python
# 스트리밍으로 답변 받기
for token in rag.query_stream("OSPF 라우팅 설정 방법은?"):
    print(token, end='', flush=True)
```

### CLI 명령어 검색

```python
# CLI 명령어만 검색
response = rag.query_cli_command("MAC 주소 테이블 확인")
print(response.answer)
```

### 번역 기능 제어

```python
# 번역 활성화/비활성화
rag.set_translation_enabled(True)   # 활성화
rag.set_translation_enabled(False)  # 비활성화
```

## 번역기 종류

### 1. Google Translate (기본)

**장점:**
- 무료로 사용 가능
- API 키 불필요
- 빠른 속도

**단점:**
- 번역 품질이 중간 수준
- 일일 요청 제한 가능

**사용법:**
```python
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="google"
)
```

### 2. DeepL (권장)

**장점:**
- 높은 번역 품질
- 기술 문서에 적합
- 월 500,000자 무료

**단점:**
- API 키 필요
- 가격 (유료 버전)

**사용법:**
```python
# .env 파일에 API 키 설정
# DEEPL_API_KEY=your_api_key

rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="deepl"
)
```

**API 키 발급:**
1. [DeepL](https://www.deepl.com/pro-api) 가입
2. API 키 생성
3. `.env` 파일에 저장

### 3. LLM 번역 (오프라인)

**장점:**
- 외부 API 불필요
- 완전 오프라인 동작
- 비용 없음

**단점:**
- 속도가 느림 (LLM 2회 호출)
- 번역 품질이 LLM 성능에 의존

**사용법:**
```python
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="llm"
)
```

### 번역기 비교

| 번역기 | 속도 | 품질 | 비용 | API 키 | 오프라인 |
|-------|------|------|------|--------|---------|
| Google | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 무료 | 불필요 | ❌ |
| DeepL | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 부분 무료 | 필요 | ❌ |
| LLM | ⭐⭐ | ⭐⭐⭐⭐ | 무료 | 불필요 | ✅ |

## 예제

### 예제 1: 기본 질의응답

```python
# 한국어 질문
question = "스위치에서 VLAN 1을 생성하는 명령어는?"

response = rag.query(question)

print(f"질문: {question}")
print(f"답변: {response.answer}")
print(f"신뢰도: {response.confidence}")
```

**출력:**
```
질문: 스위치에서 VLAN 1을 생성하는 명령어는?
답변: VLAN 1을 생성하려면 다음 명령어를 사용하세요:

1. 설정 모드 진입:
```
Switch# configure terminal
```

2. VLAN 생성:
```
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit
```

3. 설정 확인:
```
Switch# show vlan brief
```

신뢰도: 0.87
```

### 예제 2: 트러블슈팅

```python
question = "포트가 err-disabled 상태인데 어떻게 해결하나요?"

response = rag.query(question)
print(response.answer)
```

### 예제 3: 여러 질문 연속

```python
questions = [
    "STP란 무엇인가요?",
    "RSTP와 STP의 차이점은?",
    "PortFast 설정 방법은?"
]

for q in questions:
    print(f"\nQ: {q}")
    response = rag.query(q)
    print(f"A: {response.answer[:200]}...")
```

### 예제 4: 메타데이터 필터링

```python
# 특정 장비 타입으로 필터링
response = rag.query(
    question="포트 설정 방법은?",
    filter_metadata={"device_type": "Catalyst 9000"}
)

# 특정 섹션으로 필터링
response = rag.query(
    question="보안 설정 방법은?",
    filter_metadata={"section": "Security Configuration"}
)
```

## FAQ

### Q1: 번역 품질이 낮아요

**A:** 다음을 시도해보세요:

1. DeepL 사용 (품질 최고)
2. LLM 번역 사용 (더 나은 컨텍스트 이해)
3. 질문을 더 명확하게 작성

### Q2: 번역 속도가 느려요

**A:**
- Google Translate 사용 (가장 빠름)
- 스트리밍 대신 일반 쿼리 사용
- 번역 캐싱 구현 고려

### Q3: CLI 명령어가 번역되어 버려요

**A:** 코드 블록 보호 기능이 작동하지 않는 경우:

```python
# 명령어 전용 검색 사용
response = rag.query_cli_command("명령어 설명")
```

### Q4: 오프라인 환경에서 사용하고 싶어요

**A:** LLM 번역 사용:

```python
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    translator_type="llm"  # 완전 오프라인
)
```

### Q5: 영어 질문도 가능한가요?

**A:** 네, 자동 언어 감지로 처리됩니다:

```python
# 영어 질문 - 번역 없이 처리
response = rag.query("How to configure VLAN?")

# 한국어 질문 - 번역 후 처리
response = rag.query("VLAN 설정 방법은?")
```

### Q6: 비용이 얼마나 드나요?

**A:** 번역기별 비용:

- **Google Translate**: 무료 (제한적)
- **DeepL**:
  - 무료: 월 500,000자
  - 유료: $24.99/월부터
- **LLM**: 무료 (로컬 실행)

### Q7: 다른 언어도 지원하나요?

**A:** 네, 소스/타겟 언어 변경 가능:

```python
rag = create_multilingual_rag(
    vector_store=vector_store,
    llm_service=llm_service,
    source_lang="ja",  # 일본어
    manual_lang="en",  # 영어 매뉴얼
    translator_type="google"
)
```

## 고급 기능

### 커스텀 번역기 구현

```python
from src.translation.translator import BaseTranslator

class CustomTranslator(BaseTranslator):
    def translate(self, text, source_lang, target_lang):
        # 커스텀 번역 로직
        return translated_text

    def detect_language(self, text):
        # 언어 감지 로직
        return lang_code

# 사용
rag = MultilingualRAGChain(
    vector_store=vector_store,
    llm_service=llm_service,
    translator=CustomTranslator()
)
```

### 번역 캐싱

번역 결과를 캐싱하여 속도 향상:

```python
from functools import lru_cache

class CachedTranslator(BaseTranslator):
    @lru_cache(maxsize=1000)
    def translate(self, text, source_lang, target_lang):
        return self.translator.translate(text, source_lang, target_lang)
```

## 참고 자료

- [Google Translate API](https://cloud.google.com/translate)
- [DeepL API](https://www.deepl.com/docs-api)
- [LangChain Translation](https://python.langchain.com/docs/use_cases/translation)

## 라이선스

MIT License
