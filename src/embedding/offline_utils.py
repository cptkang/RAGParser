"""
오프라인 환경 감지 유틸리티

네트워크 연결 상태와 HuggingFace Hub 접근 가능 여부를 자동으로 감지합니다.
"""

import os
import socket
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def is_offline_mode() -> bool:
    """
    오프라인 모드 여부를 판단

    다음 조건 중 하나라도 만족하면 오프라인 모드로 판단:
    1. 환경 변수 HF_HUB_OFFLINE=1
    2. 환경 변수 TRANSFORMERS_OFFLINE=1
    3. 네트워크 연결 불가

    Returns:
        bool: 오프라인 모드 여부
    """
    # 환경 변수 확인
    if os.environ.get("HF_HUB_OFFLINE", "0") == "1":
        logger.info("오프라인 모드 감지: HF_HUB_OFFLINE=1")
        return True

    if os.environ.get("TRANSFORMERS_OFFLINE", "0") == "1":
        logger.info("오프라인 모드 감지: TRANSFORMERS_OFFLINE=1")
        return True

    # 네트워크 연결 확인
    if not check_network_connection():
        logger.info("오프라인 모드 감지: 네트워크 연결 불가")
        return True

    return False


def check_network_connection(
    host: str = "huggingface.co",
    port: int = 443,
    timeout: float = 3.0
) -> bool:
    """
    네트워크 연결 상태 확인

    Args:
        host: 확인할 호스트
        port: 포트 번호
        timeout: 타임아웃 (초)

    Returns:
        bool: 연결 가능 여부
    """
    try:
        # DNS 해석 및 소켓 연결 시도
        socket.create_connection((host, port), timeout=timeout)
        return True
    except (socket.timeout, socket.error, OSError):
        return False


def auto_detect_local_files_only(
    user_setting: Optional[bool] = None,
    force_check: bool = False
) -> bool:
    """
    local_files_only 설정을 자동으로 결정

    Args:
        user_setting: 사용자가 명시적으로 설정한 값 (None이면 자동 감지)
        force_check: 캐시된 결과를 무시하고 다시 확인

    Returns:
        bool: local_files_only 설정 값
    """
    # 사용자가 명시적으로 설정한 경우 그대로 사용
    if user_setting is not None:
        logger.debug(f"사용자 설정 사용: local_files_only={user_setting}")
        return user_setting

    # 캐시된 결과 사용 (불필요한 네트워크 체크 방지)
    if not force_check and hasattr(auto_detect_local_files_only, "_cached_result"):
        logger.debug("캐시된 오프라인 감지 결과 사용")
        return auto_detect_local_files_only._cached_result

    # 오프라인 모드 자동 감지
    offline = is_offline_mode()

    # 결과 캐싱
    auto_detect_local_files_only._cached_result = offline

    if offline:
        logger.info("✓ 오프라인 환경 감지 - local_files_only=True로 자동 설정")
    else:
        logger.debug("온라인 환경 - local_files_only=False")

    return offline


def check_model_cached(model_name: str) -> bool:
    """
    모델이 로컬 캐시에 있는지 확인

    Args:
        model_name: 모델 이름 또는 경로

    Returns:
        bool: 캐시 존재 여부
    """
    # 로컬 경로인 경우
    if os.path.isdir(model_name):
        logger.debug(f"로컬 모델 경로 확인: {model_name}")
        return True

    # HuggingFace 캐시 확인
    try:
        from huggingface_hub import scan_cache_dir

        cache_info = scan_cache_dir()
        model_id_normalized = model_name.replace("/", "--")

        for repo in cache_info.repos:
            if model_id_normalized in repo.repo_id:
                logger.debug(f"캐시에서 모델 발견: {model_name}")
                return True

        logger.debug(f"캐시에 모델 없음: {model_name}")
        return False

    except ImportError:
        logger.warning("huggingface_hub가 설치되지 않아 캐시 확인 불가")
        return False
    except Exception as e:
        logger.debug(f"캐시 확인 실패: {e}")
        return False


def get_offline_strategy_message() -> str:
    """
    오프라인 모드 안내 메시지 생성

    Returns:
        str: 안내 메시지
    """
    return """
오프라인 환경이 감지되었습니다.

모델을 사용하려면 먼저 온라인 환경에서 다운로드해야 합니다:

1. 온라인 환경에서 모델 다운로드:
   python scripts/download_models.py

2. 캐시 디렉토리 복사:
   - Linux/Mac: ~/.cache/huggingface/
   - Windows: C:\\Users\\<username>\\.cache\\huggingface\\

3. 오프라인 환경으로 캐시 디렉토리 이동

자세한 내용: docs/OFFLINE_USAGE.md
""".strip()
