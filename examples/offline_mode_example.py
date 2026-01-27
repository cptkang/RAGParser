#!/usr/bin/env python3
"""
오프라인 모드 자동 감지 예제

네트워크 연결 상태에 따라 자동으로 오프라인 모드를 감지하는 기능을 시연합니다.
"""

import os
import sys

# 프로젝트 루트를 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.embedding.offline_utils import (
    is_offline_mode,
    check_network_connection,
    auto_detect_local_files_only,
    check_model_cached
)
from src.embedding.embedding_service import CiscoEmbeddingService


def test_offline_detection():
    """오프라인 감지 테스트"""
    print("="*60)
    print("오프라인 환경 감지 테스트")
    print("="*60)

    # 네트워크 연결 확인
    print("\n1. 네트워크 연결 상태 확인")
    is_online = check_network_connection()
    print(f"   HuggingFace Hub 접근: {'가능' if is_online else '불가능'}")

    # 환경 변수 확인
    print("\n2. 환경 변수 확인")
    hf_offline = os.environ.get("HF_HUB_OFFLINE", "0")
    transformers_offline = os.environ.get("TRANSFORMERS_OFFLINE", "0")
    print(f"   HF_HUB_OFFLINE={hf_offline}")
    print(f"   TRANSFORMERS_OFFLINE={transformers_offline}")

    # 오프라인 모드 판단
    print("\n3. 오프라인 모드 판단")
    offline_mode = is_offline_mode()
    print(f"   오프라인 모드: {offline_mode}")

    # local_files_only 자동 설정
    print("\n4. local_files_only 자동 설정")
    local_files_only = auto_detect_local_files_only()
    print(f"   local_files_only={local_files_only}")

    print("\n" + "="*60)
    print("✓ 테스트 완료")
    print("="*60)


def test_model_loading():
    """모델 로딩 테스트 (자동 감지)"""
    print("\n\n" + "="*60)
    print("모델 로딩 테스트 (자동 오프라인 감지)")
    print("="*60)

    model_name = "BAAI/bge-m3"

    print(f"\n모델: {model_name}")
    print("local_files_only: None (자동 감지)")

    try:
        # local_files_only를 지정하지 않으면 자동으로 감지
        service = CiscoEmbeddingService(
            model_name=model_name,
            # local_files_only는 지정하지 않음 (자동 감지)
        )

        print(f"\n✓ 모델 로드 성공!")
        print(f"  - Dimension: {service.dimension}")
        print(f"  - Device: {service.device}")
        print(f"  - Offline mode: {service.local_files_only}")

    except Exception as e:
        print(f"\n✗ 모델 로드 실패: {e}")


def test_explicit_mode():
    """명시적 모드 설정 테스트"""
    print("\n\n" + "="*60)
    print("명시적 모드 설정 테스트")
    print("="*60)

    model_name = "BAAI/bge-m3"

    # 1. 명시적으로 온라인 모드
    print("\n1. 명시적으로 온라인 모드 (local_files_only=False)")
    try:
        service = CiscoEmbeddingService(
            model_name=model_name,
            local_files_only=False
        )
        print(f"   ✓ 모델 로드 성공 (offline={service.local_files_only})")
    except Exception as e:
        print(f"   ✗ 실패: {type(e).__name__}")

    # 2. 명시적으로 오프라인 모드
    print("\n2. 명시적으로 오프라인 모드 (local_files_only=True)")
    try:
        service = CiscoEmbeddingService(
            model_name=model_name,
            local_files_only=True
        )
        print(f"   ✓ 모델 로드 성공 (offline={service.local_files_only})")
    except Exception as e:
        print(f"   ✗ 실패: {type(e).__name__}")


def test_with_env_variable():
    """환경 변수를 사용한 테스트"""
    print("\n\n" + "="*60)
    print("환경 변수 설정 테스트")
    print("="*60)

    # 환경 변수 설정
    print("\n환경 변수 HF_HUB_OFFLINE=1 설정")
    os.environ["HF_HUB_OFFLINE"] = "1"

    # 캐시 무효화 (강제 재검사)
    if hasattr(auto_detect_local_files_only, "_cached_result"):
        delattr(auto_detect_local_files_only, "_cached_result")

    # 자동 감지 테스트
    local_files_only = auto_detect_local_files_only(force_check=True)
    print(f"자동 감지 결과: local_files_only={local_files_only}")

    # 환경 변수 제거
    del os.environ["HF_HUB_OFFLINE"]

    # 캐시 무효화
    if hasattr(auto_detect_local_files_only, "_cached_result"):
        delattr(auto_detect_local_files_only, "_cached_result")


def main():
    """메인 함수"""
    print("오프라인 모드 자동 감지 예제\n")

    # 1. 오프라인 감지 테스트
    test_offline_detection()

    # 2. 환경 변수 테스트
    test_with_env_variable()

    # 3. 명시적 모드 테스트
    test_explicit_mode()

    # 4. 모델 로딩 테스트 (실제로 모델을 로드하려면 주석 해제)
    # test_model_loading()

    print("\n\n" + "="*60)
    print("모든 테스트 완료!")
    print("="*60)
    print("\n실제 모델 로딩을 테스트하려면:")
    print("  test_model_loading() 함수의 주석을 해제하세요.")


if __name__ == "__main__":
    main()
