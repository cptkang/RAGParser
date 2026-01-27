# 오프라인 자동 감지 기능 (v2.0)

## 개요

네트워크 연결 상태를 자동으로 감지하여 임베딩 모델을 로컬 캐시에서 로드하는 기능입니다.

더 이상 `local_files_only=True`를 수동으로 설정할 필요가 없습니다!

## 주요 기능

### 1. 자동 네트워크 감지
- HuggingFace Hub 접근 가능 여부를 자동으로 확인
- 3초 타임아웃으로 빠른 감지
- 네트워크 연결 불가 시 자동으로 오프라인 모드 활성화

### 2. 환경 변수 지원
- `HF_HUB_OFFLINE=1`: HuggingFace Hub 오프라인 모드
- `TRANSFORMERS_OFFLINE=1`: Transformers 라이브러리 오프라인 모드
- 환경 변수가 설정되면 네트워크 확인 없이 즉시 오프라인 모드

### 3. 명시적 제어 가능
- `local_files_only=None`: 자동 감지 (기본값)
- `local_files_only=True`: 강제 오프라인 모드
- `local_files_only=False`: 강제 온라인 모드

### 4. 성능 최적화
- 감지 결과 캐싱으로 불필요한 네트워크 체크 방지
- 첫 번째 모델 로드 시 한 번만 확인

## 사용 방법

### 기본 사용 (자동 감지)

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# local_files_only를 지정하지 않으면 자동 감지
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
)

# 온라인 환경: 네트워크에서 모델 다운로드 또는 캐시 사용
# 오프라인 환경: 자동으로 로컬 캐시만 사용
```

### 환경 변수 사용

```bash
# Linux/Mac
export HF_HUB_OFFLINE=1

# Windows (PowerShell)
$env:HF_HUB_OFFLINE=1

# Python 코드에서
import os
os.environ['HF_HUB_OFFLINE'] = '1'
```

```python
# 환경 변수가 설정되면 자동으로 오프라인 모드
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
)
print(f"Offline: {service.local_files_only}")  # True
```

### 명시적 제어

```python
# 온라인 모드 강제
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=False  # 자동 감지 무시
)

# 오프라인 모드 강제
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=True  # 자동 감지 무시
)
```

## 작동 순서

```
1. local_files_only 파라미터 확인
   └─> None이 아니면: 사용자 설정값 사용
   └─> None이면: 다음 단계로

2. 환경 변수 확인
   └─> HF_HUB_OFFLINE=1 또는 TRANSFORMERS_OFFLINE=1
       └─> 오프라인 모드 (True)

3. 네트워크 연결 테스트
   └─> huggingface.co:443 연결 시도 (3초 타임아웃)
       ├─> 성공: 온라인 모드 (False)
       └─> 실패: 오프라인 모드 (True)

4. 오프라인 모드 활성화 (자동)
   └─> 환경 변수 자동 설정: HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1
       └─> 모든 HuggingFace Hub 접근 차단
       └─> SentenceTransformer가 API 호출 시도 방지

5. 결과 캐싱
   └─> 다음 모델 로드 시 재사용
```

## 테스트

### 자동 감지 테스트

```bash
python examples/offline_mode_example.py
```

출력:
```
============================================================
오프라인 환경 감지 테스트
============================================================

1. 네트워크 연결 상태 확인
   HuggingFace Hub 접근: 가능

2. 환경 변수 확인
   HF_HUB_OFFLINE=0
   TRANSFORMERS_OFFLINE=0

3. 오프라인 모드 판단
   오프라인 모드: False

4. local_files_only 자동 설정
   local_files_only=False
```

### 유닛 테스트

```python
from src.embedding.offline_utils import (
    check_network_connection,
    is_offline_mode,
    auto_detect_local_files_only
)

# 네트워크 연결 확인
assert check_network_connection() == True  # 온라인 환경

# 오프라인 모드 감지
assert is_offline_mode() == False  # 온라인 환경

# local_files_only 자동 설정
assert auto_detect_local_files_only() == False  # 온라인 환경
```

## API 레퍼런스

### `check_network_connection(host, port, timeout)`

네트워크 연결 상태 확인

**Parameters:**
- `host` (str): 확인할 호스트 (기본값: "huggingface.co")
- `port` (int): 포트 번호 (기본값: 443)
- `timeout` (float): 타임아웃 초 (기본값: 3.0)

**Returns:**
- `bool`: 연결 가능 여부

### `is_offline_mode()`

오프라인 모드 여부 판단

**Returns:**
- `bool`: 오프라인 모드 여부

### `auto_detect_local_files_only(user_setting, force_check)`

`local_files_only` 설정 자동 결정

**Parameters:**
- `user_setting` (Optional[bool]): 사용자가 명시적으로 설정한 값 (None이면 자동 감지)
- `force_check` (bool): 캐시 무시하고 재검사 (기본값: False)

**Returns:**
- `bool`: local_files_only 설정 값

## 마이그레이션 가이드

### 기존 코드 (v1.x)

```python
# 수동으로 오프라인 모드 설정
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=True  # 수동 설정 필요
)
```

### 새로운 코드 (v2.0+)

```python
# 자동으로 감지!
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
    # local_files_only는 자동 감지됨
)
```

**변경 필요 없음!** 기존 코드도 그대로 작동합니다.

## 장점

1. **편리성**: 코드 수정 없이 환경에 따라 자동 대응
2. **안정성**: 네트워크 오류 시 자동으로 로컬 캐시 사용
3. **완벽한 오프라인**: 환경 변수 자동 설정으로 모든 HuggingFace Hub 접근 차단
4. **유연성**: 환경 변수나 명시적 설정으로 제어 가능
5. **성능**: 결과 캐싱으로 빠른 실행
6. **호환성**: 기존 코드와 완벽 호환

## 제한 사항

1. **첫 실행 시 3초 지연**: 네트워크 연결 확인에 최대 3초 소요
   - 해결책: 환경 변수를 사용하면 즉시 판단

2. **캐시 의존**: 오프라인 모드는 로컬 캐시가 필요
   - 해결책: 미리 `python scripts/download_models.py`로 모델 다운로드

3. **동적 네트워크 변화**: 실행 중 네트워크 상태 변화는 감지 불가
   - 해결책: `force_check=True`로 재검사 또는 재시작

## 트러블슈팅

### 문제 1: 오프라인인데 온라인으로 감지됨

**원인**: 로컬 네트워크는 연결되어 있지만 HuggingFace Hub 접근 불가

**해결:**
```bash
export HF_HUB_OFFLINE=1
```

### 문제 2: 온라인인데 오프라인으로 감지됨

**원인**: 방화벽이나 프록시로 인한 연결 실패

**해결:**
```python
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=False  # 명시적으로 온라인 모드 사용
)
```

### 문제 3: 감지가 너무 느림

**원인**: 네트워크 타임아웃 대기 중

**해결:**
```bash
# 환경 변수로 즉시 판단
export HF_HUB_OFFLINE=1
```

### 문제 4: local_files_only=True인데도 HuggingFace API 접근 시도 ⭐ NEW

**증상**:
```
ConnectionError: HTTPSConnectionPool(host='huggingface.co', port=443):
Max retries exceeded with url: /api/models/BAAI/bge-m3
```

**원인**: `SentenceTransformer` 내부에서 `local_files_only=True`를 설정해도 `huggingface_hub` 라이브러리가 모델 메타데이터를 조회하기 위해 API를 호출

**해결**: **v2.1부터 자동 해결됨!**
- 오프라인 모드가 감지되면 자동으로 `HF_HUB_OFFLINE=1` 및 `TRANSFORMERS_OFFLINE=1` 환경 변수 설정
- 모든 HuggingFace Hub 접근이 완전히 차단됨
- 코드 수정 불필요

**수동 해결 (이전 버전)**:
```python
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'

from src.embedding.embedding_service import CiscoEmbeddingService
service = CiscoEmbeddingService(model_name="BAAI/bge-m3")
```

## 관련 문서

- [오프라인 사용 가이드](OFFLINE_USAGE.md) - 전체 오프라인 사용 방법
- [설정 가이드](../SETUP_COMPLETE.md) - 시스템 전체 설정
- [임베딩 전략 가이드](../EMBEDDING_STRATEGY_GUIDE.md) - 모델 선택 및 최적화
