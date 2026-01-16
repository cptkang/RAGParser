# src/splitter/test_splitter.py

from cisco_splitter import CiscoManualSplitter
from pathlib import Path


def test_splitter():
    """스플리터 테스트"""
    
    # 테스트용 샘플 문서
    sample_markdown = """
# Chapter 1: VLAN 설정

## 1.1 VLAN 개요

VLAN(Virtual Local Area Network)은 물리적 위치와 관계없이 논리적으로 네트워크를 
분할하는 기술입니다. 이를 통해 브로드캐스트 도메인을 분리하고 네트워크 보안을 
향상시킬 수 있습니다.

### 1.1.1 VLAN의 장점

- 브로드캐스트 트래픽 감소
- 보안 향상
- 유연한 네트워크 관리
- 비용 절감

## 1.2 VLAN 설정 방법

### 1.2.1 VLAN 생성

다음 명령어를 사용하여 VLAN을 생성합니다:
```cisco-ios
Switch> enable
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
Switch(config-vlan)# exit
Switch(config)# vlan 20
Switch(config-vlan)# name ENGINEERING
Switch(config-vlan)# exit
```

> **WARNING**
> VLAN 1은 기본 VLAN이므로 삭제할 수 없습니다.

### 1.2.2 포트 할당

인터페이스에 VLAN을 할당하는 방법:
```cisco-ios
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit
```

| 포트 | VLAN | 설명 |
|------|------|------|
| Gi0/1 | 10 | 영업팀 |
| Gi0/2 | 10 | 영업팀 |
| Gi0/3 | 20 | 개발팀 |
| Gi0/4 | 20 | 개발팀 |

## 1.3 VLAN 확인

설정된 VLAN을 확인하려면 다음 명령어를 사용합니다:
```cisco-ios
Switch# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi0/5, Gi0/6
10   SALES                            active    Gi0/1, Gi0/2
20   ENGINEERING                      active    Gi0/3, Gi0/4
```
"""

    # 스플리터 초기화
    splitter = CiscoManualSplitter(
        chunk_size=500,
        chunk_overlap=50,
        preserve_cli_blocks=True
    )
    
    # 문서 분할
    metadata = {
        'source': 'cisco_catalyst_manual.pdf',
        'chapter': 'VLAN Configuration',
        'device': 'Catalyst 9000'
    }
    
    chunks = splitter.split_document(sample_markdown, metadata)
    
    # 결과 출력
    print(f"\n총 {len(chunks)}개 청크 생성\n")
    print("=" * 80)
    
    for i, chunk in enumerate(chunks):
        print(f"\n[청크 {i+1}]")
        print(f"타입: {chunk.metadata.get('chunk_type', 'unknown')}")
        print(f"토큰: {chunk.metadata.get('token_count', 'N/A')}")
        print(f"키워드: {chunk.metadata.get('keywords', [])}")
        print(f"섹션: {chunk.metadata.get('section', 'N/A')}")
        print("-" * 40)
        print(chunk.page_content[:300] + "..." if len(chunk.page_content) > 300 else chunk.page_content)
        print("=" * 80)
    
    return chunks


if __name__ == "__main__":
    test_splitter()