# NLTK 데이터 오프라인 설치 가이드

## 개요

`unstructured` 라이브러리는 내부적으로 NLTK를 사용합니다. 오프라인 환경에서는 NLTK 데이터를 자동으로 다운로드할 수 없어 다음과 같은 에러가 발생합니다:

```
[nltk_data] Error loading averaged_perceptron_tagger_eng: <urlopen error [WinError 10061]>
[nltk_data] Error loading punkt_tab: <urlopen error [WinError 10061]>
```

이 가이드는 오프라인 환경에서 NLTK 데이터를 설치하는 방법을 설명합니다.

---

## 필요한 NLTK 데이터

| 데이터 이름 | 용도 |
|------------|------|
| `punkt_tab` | 문장 토큰화 |
| `punkt` | 문장 토큰화 (레거시) |
| `averaged_perceptron_tagger_eng` | 품사 태깅 |

---

## 방법 1: 온라인 환경에서 미리 다운로드

인터넷이 가능한 환경에서 Python을 실행하여 데이터를 다운로드합니다.

```python
import nltk

# 필요한 데이터 다운로드
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')
nltk.download('punkt')

# 다운로드 경로 확인
print(nltk.data.path)
```

### 기본 다운로드 경로

| OS | 경로 |
|----|------|
| Windows | `C:\Users\<username>\nltk_data` |
| Linux | `~/nltk_data` 또는 `/usr/share/nltk_data` |
| macOS | `~/nltk_data` |

---

## 방법 2: 수동 다운로드 (오프라인 설치)

### Step 1: 데이터 파일 다운로드

온라인 환경에서 아래 URL의 파일을 다운로드합니다:

| 데이터 | 다운로드 URL |
|--------|-------------|
| punkt_tab | https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt_tab.zip |
| punkt | https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip |
| averaged_perceptron_tagger_eng | https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/taggers/averaged_perceptron_tagger_eng.zip |

### Step 2: 오프라인 PC에 설치

#### Windows

```powershell
# 디렉토리 생성
mkdir C:\Users\%USERNAME%\nltk_data\tokenizers
mkdir C:\Users\%USERNAME%\nltk_data\taggers

# 압축 해제 (PowerShell)
Expand-Archive -Path punkt_tab.zip -DestinationPath C:\Users\%USERNAME%\nltk_data\tokenizers\
Expand-Archive -Path punkt.zip -DestinationPath C:\Users\%USERNAME%\nltk_data\tokenizers\
Expand-Archive -Path averaged_perceptron_tagger_eng.zip -DestinationPath C:\Users\%USERNAME%\nltk_data\taggers\
```

#### Linux

```bash
# 디렉토리 생성
mkdir -p ~/nltk_data/tokenizers
mkdir -p ~/nltk_data/taggers

# 압축 해제
unzip punkt_tab.zip -d ~/nltk_data/tokenizers/
unzip punkt.zip -d ~/nltk_data/tokenizers/
unzip averaged_perceptron_tagger_eng.zip -d ~/nltk_data/taggers/
```

### 최종 디렉토리 구조

```
nltk_data/
├── tokenizers/
│   ├── punkt_tab/
│   │   └── english/
│   │       └── ...
│   └── punkt/
│       └── english.pickle
└── taggers/
    └── averaged_perceptron_tagger_eng/
        └── averaged_perceptron_tagger_eng.pickle
```

---

## 방법 3: 프로젝트 내 로컬 경로 사용 (권장)

프로젝트와 함께 NLTK 데이터를 배포하여 환경에 관계없이 동작하도록 설정합니다.

### Step 1: 프로젝트 내 nltk_data 폴더 생성

```
RAGParser/
├── nltk_data/
│   ├── tokenizers/
│   │   ├── punkt_tab/
│   │   └── punkt/
│   └── taggers/
│       └── averaged_perceptron_tagger_eng/
├── src/
└── ...
```

### Step 2: 코드에서 경로 설정

프로젝트 초기화 시 NLTK 데이터 경로를 설정합니다:

```python
import nltk
import os
from pathlib import Path

def setup_nltk_data():
    """오프라인 환경을 위한 NLTK 데이터 경로 설정"""
    # 프로젝트 루트의 nltk_data 폴더
    project_root = Path(__file__).resolve().parent.parent.parent
    nltk_data_path = project_root / 'nltk_data'

    if nltk_data_path.exists():
        # 프로젝트 경로를 최우선으로 추가
        nltk.data.path.insert(0, str(nltk_data_path))
        return True
    return False

# 모듈 로드 시 자동 설정
setup_nltk_data()
```

### Step 3: 데이터 복사 스크립트

온라인 환경에서 데이터를 프로젝트로 복사하는 스크립트:

```python
# scripts/copy_nltk_data.py
import nltk
import shutil
from pathlib import Path

def copy_nltk_to_project():
    """시스템 NLTK 데이터를 프로젝트로 복사"""
    project_root = Path(__file__).resolve().parent.parent
    target_dir = project_root / 'nltk_data'

    # 필요한 데이터 목록
    required_data = [
        ('tokenizers', 'punkt_tab'),
        ('tokenizers', 'punkt'),
        ('taggers', 'averaged_perceptron_tagger_eng'),
    ]

    for category, name in required_data:
        try:
            # NLTK에서 데이터 경로 찾기
            source = Path(nltk.data.find(f'{category}/{name}'))
            dest = target_dir / category / name

            dest.parent.mkdir(parents=True, exist_ok=True)

            if source.is_dir():
                shutil.copytree(source, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(source, dest)

            print(f"Copied: {name}")
        except LookupError:
            print(f"Not found: {name} - downloading...")
            nltk.download(name)
            # 다운로드 후 재시도
            copy_nltk_to_project()
            return

    print(f"\nNLTK data copied to: {target_dir}")

if __name__ == '__main__':
    copy_nltk_to_project()
```

---

## 방법 4: 환경 변수 설정

시스템 환경 변수로 NLTK 데이터 경로를 지정합니다.

### Windows

```powershell
# 임시 설정 (현재 세션)
set NLTK_DATA=G:\RAGParser\nltk_data

# 영구 설정 (시스템 환경 변수)
setx NLTK_DATA "G:\RAGParser\nltk_data"
```

### Linux

```bash
# 임시 설정 (현재 세션)
export NLTK_DATA=~/projects/RAGParser/nltk_data

# 영구 설정 (~/.bashrc 또는 ~/.zshrc에 추가)
echo 'export NLTK_DATA=~/projects/RAGParser/nltk_data' >> ~/.bashrc
source ~/.bashrc
```

---

## 설치 확인

설치가 정상적으로 되었는지 확인합니다:

```python
import nltk

# 데이터 경로 확인
print("NLTK Data Paths:")
for path in nltk.data.path:
    print(f"  - {path}")

# 데이터 찾기 테스트
try:
    punkt = nltk.data.find('tokenizers/punkt_tab')
    print(f"\npunkt_tab: {punkt}")
except LookupError as e:
    print(f"\npunkt_tab: NOT FOUND - {e}")

try:
    tagger = nltk.data.find('taggers/averaged_perceptron_tagger_eng')
    print(f"averaged_perceptron_tagger_eng: {tagger}")
except LookupError as e:
    print(f"averaged_perceptron_tagger_eng: NOT FOUND - {e}")
```

---

## 문제 해결

### 여전히 다운로드 시도하는 경우

NLTK가 로컬 데이터를 찾지 못하면 자동 다운로드를 시도합니다. 다음을 확인하세요:

1. **폴더 구조 확인**: `punkt_tab/` 폴더 안에 실제 데이터 파일이 있는지 확인
2. **권한 확인**: Linux에서 읽기 권한이 있는지 확인
3. **경로 우선순위**: `nltk.data.path.insert(0, ...)` 로 로컬 경로를 최우선으로 설정

### 자동 다운로드 비활성화

네트워크 요청 자체를 차단하려면:

```python
import nltk
nltk.download = lambda *args, **kwargs: None  # 다운로드 함수 비활성화
```

---

## 권장 사항

| 환경 | 권장 방법 |
|------|----------|
| 개발 환경 (온라인) | 방법 1 (자동 다운로드) |
| 운영 환경 (오프라인) | 방법 3 (프로젝트 내 포함) |
| Docker / CI/CD | 방법 3 + Dockerfile에서 복사 |
| 다중 프로젝트 공유 | 방법 4 (환경 변수) |

---

## 참고 링크

- [NLTK Data Repository](https://github.com/nltk/nltk_data)
- [NLTK 공식 문서](https://www.nltk.org/data.html)
- [NLTK Data 전체 목록](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml)
