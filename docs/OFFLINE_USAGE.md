# 오프라인 환경에서 임베딩 모델 사용하기

이 가이드는 네트워크 연결이 없는 환경에서 임베딩 모델을 사용하는 방법을 설명합니다.

## 목차
1. [개요](#개요)
2. [자동 오프라인 감지 (권장)](#자동-오프라인-감지-권장)
3. [방법 1: HuggingFace 캐시 사용](#방법-1-huggingface-캐시-사용)
4. [방법 2: 로컬 디렉토리에 저장](#방법-2-로컬-디렉토리에-저장)
5. [방법 3: 환경 변수 설정](#방법-3-환경-변수-설정)
6. [트러블슈팅](#트러블슈팅)

---

## 개요

기본적으로 `sentence-transformers`는 모델을 HuggingFace Hub에서 다운로드합니다.
오프라인 환경에서 사용하려면 다음 두 단계가 필요합니다:

1. **온라인 환경**: 모델을 미리 다운로드
2. **오프라인 환경**: 다운로드한 모델 사용

### ⭐ 자동 오프라인 감지 기능

**v2.0부터는 네트워크 연결 상태를 자동으로 감지하여 오프라인 모드를 활성화합니다!**

더 이상 `local_files_only=True`를 수동으로 설정할 필요가 없습니다. 시스템이 다음을 자동으로 확인합니다:
- 네트워크 연결 상태
- HuggingFace Hub 접근 가능 여부
- 환경 변수 설정

---

## 자동 오프라인 감지 (권장)

### 1단계: 온라인 환경에서 모델 다운로드

```bash
# 기본 모델 다운로드
python scripts/download_models.py

# 캐시 위치 확인
# - Linux/Mac: ~/.cache/huggingface/
# - Windows: C:\Users\<username>\.cache\huggingface\
```

### 2단계: 캐시를 오프라인 환경으로 복사

```bash
# 온라인 환경에서
tar -czf huggingface_cache.tar.gz ~/.cache/huggingface/

# 오프라인 환경으로 전송 후
tar -xzf huggingface_cache.tar.gz -C ~/
```

### 3단계: 코드에서 그냥 사용!

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# local_files_only를 지정하지 않아도 자동으로 감지!
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
    # local_files_only는 자동으로 True로 설정됨
)

# 서비스가 자동으로 오프라인 모드를 감지하고 로컬 캐시 사용
results = service.embed_documents(documents)
```

### 작동 원리

시스템은 다음 순서로 오프라인 모드를 판단합니다:

1. **환경 변수 확인**
   - `HF_HUB_OFFLINE=1` 또는 `TRANSFORMERS_OFFLINE=1`이 설정되어 있으면 오프라인 모드

2. **네트워크 연결 테스트**
   - `huggingface.co:443`에 3초 이내 연결 시도
   - 연결 실패 시 오프라인 모드

3. **자동 결정**
   - 위 조건에 따라 `local_files_only`를 자동 설정

### 자동 감지 테스트

```bash
# 오프라인 감지 테스트 실행
python examples/offline_mode_example.py
```

출력 예시:
```
오프라인 환경 감지 테스트
====================================
1. 네트워크 연결 상태 확인
   HuggingFace Hub 접근: 불가능

2. 환경 변수 확인
   HF_HUB_OFFLINE=0
   TRANSFORMERS_OFFLINE=0

3. 오프라인 모드 판단
   오프라인 모드: True

4. local_files_only 자동 설정
   local_files_only=True
```

---

---

## 방법 1: HuggingFace 캐시 사용

이 방법은 가장 간단하며, HuggingFace의 기본 캐시 디렉토리를 사용합니다.

### 1단계: 온라인 환경에서 모델 다운로드

```bash
# 기본 모델 다운로드 (BAAI/bge-m3, BAAI/bge-large-en-v1.5)
python scripts/download_models.py

# 특정 모델만 다운로드
python scripts/download_models.py --models "BAAI/bge-m3"

# 여러 모델 다운로드
python scripts/download_models.py --models "BAAI/bge-m3" "BAAI/bge-large-en-v1.5"
```

모델은 기본적으로 다음 위치에 캐시됩니다:
- Linux/Mac: `~/.cache/huggingface/hub/`
- Windows: `C:\Users\<username>\.cache\huggingface\hub\`

### 2단계: 캐시 디렉토리를 오프라인 환경으로 복사

```bash
# 온라인 환경에서
tar -czf huggingface_cache.tar.gz ~/.cache/huggingface/

# 오프라인 환경으로 파일 전송 후
tar -xzf huggingface_cache.tar.gz -C ~/
```

### 3단계: 오프라인 환경에서 코드 사용

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# local_files_only=True로 설정
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=True  # 오프라인 모드 활성화
)
```

또는 DualEmbeddingService 사용:

```python
from src.embedding.dual_embedding_service import create_embedding_service

service = create_embedding_service(
    strategy="dual",
    document_model="BAAI/bge-large-en-v1.5",
    local_files_only=True  # 오프라인 모드 활성화
)
```

---

## 방법 2: 로컬 디렉토리에 저장

특정 디렉토리에 모델을 저장하고 해당 경로를 직접 지정하는 방법입니다.

### 1단계: 온라인 환경에서 특정 디렉토리에 모델 저장

```bash
# models/ 디렉토리에 저장
python scripts/download_models.py --save-dir ./models

# 결과:
# ./models/BAAI_bge-m3/
# ./models/BAAI_bge-large-en-v1.5/
```

### 2단계: 모델 디렉토리를 오프라인 환경으로 복사

```bash
# 온라인 환경에서
tar -czf models.tar.gz ./models/

# 오프라인 환경으로 전송 후
tar -xzf models.tar.gz
```

### 3단계: 로컬 경로로 모델 로드

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# 로컬 경로 사용 (local_files_only는 자동으로 True)
service = CiscoEmbeddingService(
    model_name="./models/BAAI_bge-m3"
)
```

---

## 방법 3: 환경 변수 설정

시스템 전체에서 오프라인 모드를 활성화하려면 환경 변수를 설정할 수 있습니다.

### Linux/Mac

```bash
# 환경 변수 설정
export HF_HUB_OFFLINE=1

# 또는 .bashrc / .zshrc에 추가
echo 'export HF_HUB_OFFLINE=1' >> ~/.bashrc
source ~/.bashrc

# 이제 코드에서 local_files_only 없이 사용 가능
python your_script.py
```

### Windows (PowerShell)

```powershell
# 환경 변수 설정
$env:HF_HUB_OFFLINE=1

# 영구 설정
[System.Environment]::SetEnvironmentVariable('HF_HUB_OFFLINE', '1', 'User')
```

### Python 코드에서 설정

```python
import os
os.environ['HF_HUB_OFFLINE'] = '1'

from src.embedding.embedding_service import CiscoEmbeddingService

# 환경 변수가 설정되어 있으면 자동으로 오프라인 모드
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
)
```

---

## 사용 예제

### 예제 1: 자동 감지 (권장) ⭐

```python
from src.embedding.embedding_service import CiscoEmbeddingService
from langchain_core.documents import Document

# 자동으로 오프라인 모드 감지!
# local_files_only를 지정하지 않아도 됨
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
)

# 문서 임베딩
documents = [
    Document(page_content="Configure VLAN 100", metadata={"type": "command"}),
    Document(page_content="show vlan brief", metadata={"type": "command"})
]

results = service.embed_documents(documents)

# 쿼리 임베딩
query_embedding = service.embed_query("How to configure VLAN?")
```

### 예제 2: 명시적 오프라인 모드

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# 명시적으로 오프라인 모드 지정
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=True  # 명시적 설정
)

# 사용
results = service.embed_documents(documents)
```

### 예제 3: DualEmbeddingService (자동 감지)

```python
from src.embedding.dual_embedding_service import create_embedding_service

# 자동 오프라인 감지
service = create_embedding_service(
    strategy="dual",
    document_model="BAAI/bge-large-en-v1.5"
    # local_files_only는 자동 감지됨
)

# 또는 로컬 경로 직접 사용
service = create_embedding_service(
    strategy="dual",
    document_model="./models/BAAI_bge-large-en-v1.5"
)

# 사용
results = service.embed_documents(documents)
query_embedding = service.embed_query("Your query here")
```

### 예제 4: 환경 변수 활용

```python
import os

# 프로그램 시작 시 환경 변수 설정
os.environ['HF_HUB_OFFLINE'] = '1'

from src.embedding.embedding_service import CiscoEmbeddingService

# 환경 변수가 설정되어 있으므로 자동으로 오프라인 모드
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3"
)

print(f"Offline mode: {service.local_files_only}")  # True
```

### 예제 5: 명시적 온라인 모드 강제

```python
from src.embedding.embedding_service import CiscoEmbeddingService

# 오프라인 환경이지만 온라인 모드를 강제하고 싶을 때
# (예: 새 모델 다운로드)
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=False  # 자동 감지 무시하고 온라인 모드 사용
)
```

---

## 트러블슈팅

### 문제 1: OSError: Can't load the model

**증상:**
```
OSError: Can't load the model for 'BAAI/bge-m3'. If you were trying to load it from 'https://huggingface.co/models'...
```

**해결 방법:**
1. 모델이 제대로 다운로드되었는지 확인:
   ```bash
   ls ~/.cache/huggingface/hub/
   ```

2. 캐시 디렉토리가 올바른지 확인:
   ```python
   from huggingface_hub import snapshot_download
   print(snapshot_download.cache_dir)
   ```

3. 모델을 다시 다운로드:
   ```bash
   python scripts/download_models.py
   ```

### 문제 2: 권한 오류

**증상:**
```
PermissionError: [Errno 13] Permission denied
```

**해결 방법:**
```bash
# 캐시 디렉토리 권한 확인
chmod -R 755 ~/.cache/huggingface/

# 또는 sudo 없이 쓰기 가능한 디렉토리 사용
export HF_HOME=/path/to/writable/directory
```

### 문제 3: 디스크 공간 부족

**증상:**
```
OSError: [Errno 28] No space left on device
```

**해결 방법:**

모델 크기 확인:
- `BAAI/bge-m3`: ~2.24 GB
- `BAAI/bge-large-en-v1.5`: ~1.34 GB

충분한 디스크 공간(최소 5GB 이상)을 확보하세요.

### 문제 4: 네트워크 연결 시도

**증상:**
오프라인 환경인데도 네트워크 연결을 시도함

**해결 방법:**
1. `local_files_only=True` 파라미터가 제대로 전달되었는지 확인
2. 환경 변수 확인:
   ```python
   import os
   print(os.environ.get('HF_HUB_OFFLINE'))
   ```

3. 모델명이 정확한지 확인 (대소문자 구분)

---

## 추가 정보

### 캐시 디렉토리 위치 확인

```python
import os
from pathlib import Path

# HuggingFace 캐시 위치
hf_cache = os.environ.get(
    'HF_HOME',
    os.path.join(Path.home(), '.cache', 'huggingface')
)
print(f"HuggingFace cache: {hf_cache}")

# sentence-transformers 캐시 위치
st_cache = os.environ.get(
    'SENTENCE_TRANSFORMERS_HOME',
    os.path.join(Path.home(), '.cache', 'torch', 'sentence_transformers')
)
print(f"SentenceTransformers cache: {st_cache}")
```

### 캐시 디렉토리 변경

```python
import os

# HuggingFace 캐시 위치 변경
os.environ['HF_HOME'] = '/custom/path/to/cache'

# 또는 프로젝트 디렉토리 내부로
os.environ['HF_HOME'] = './cache/huggingface'
```

### 모델 파일 확인

다운로드된 모델의 파일 구조:
```
~/.cache/huggingface/hub/models--BAAI--bge-m3/
├── snapshots/
│   └── <hash>/
│       ├── config.json
│       ├── model.safetensors (또는 pytorch_model.bin)
│       ├── tokenizer.json
│       ├── tokenizer_config.json
│       └── ...
└── ...
```

---

## 요약

### ⭐ 최고의 방법: 자동 오프라인 감지 (v2.0+)

1. 온라인 환경에서 모델 다운로드:
   ```bash
   python scripts/download_models.py
   ```

2. 캐시 디렉토리를 오프라인 환경으로 복사:
   ```bash
   tar -czf huggingface_cache.tar.gz ~/.cache/huggingface/
   # 오프라인 환경으로 전송 후
   tar -xzf huggingface_cache.tar.gz -C ~/
   ```

3. 코드에서 자동 감지 사용:
   ```python
   from src.embedding.embedding_service import CiscoEmbeddingService

   # local_files_only 지정 불필요!
   service = CiscoEmbeddingService(model_name="BAAI/bge-m3")
   ```

**장점:**
- ✓ 자동 감지로 코드 간소화
- ✓ 네트워크 환경 변화에 자동 대응
- ✓ 환경 변수를 통한 전역 제어 가능
- ✓ HuggingFace 표준 방식 준수

### 기존 방법도 여전히 사용 가능

명시적으로 `local_files_only=True/False`를 지정하여 자동 감지를 무시할 수 있습니다.

```python
# 명시적 오프라인 모드
service = CiscoEmbeddingService(
    model_name="BAAI/bge-m3",
    local_files_only=True
)
```
