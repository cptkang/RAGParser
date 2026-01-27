#!/usr/bin/env python3
"""
임베딩 모델 다운로드 스크립트

오프라인 환경에서 사용하기 위해 모델을 미리 다운로드합니다.
"""

import os
import argparse
from pathlib import Path
from sentence_transformers import SentenceTransformer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 프로젝트에서 사용하는 모델 리스트
DEFAULT_MODELS = [
    "BAAI/bge-m3",                    # BGE-M3 다국어 모델
    "BAAI/bge-large-en-v1.5",        # BGE Large English 모델
]


def download_model(model_name: str, save_dir: str = None):
    """
    모델을 다운로드하고 로컬에 저장

    Args:
        model_name: HuggingFace 모델명
        save_dir: 저장할 디렉토리 (None이면 기본 캐시 사용)
    """
    try:
        logger.info(f"Downloading model: {model_name}")

        if save_dir:
            # 지정된 디렉토리에 저장
            os.makedirs(save_dir, exist_ok=True)
            model_path = Path(save_dir) / model_name.replace("/", "_")

            logger.info(f"Saving to: {model_path}")
            model = SentenceTransformer(model_name)
            model.save(str(model_path))

            logger.info(f"✓ Successfully saved to {model_path}")
            return str(model_path)
        else:
            # HuggingFace 캐시에 다운로드
            logger.info("Saving to HuggingFace cache")
            model = SentenceTransformer(model_name)

            logger.info(f"✓ Successfully cached {model_name}")
            return model_name

    except Exception as e:
        logger.error(f"✗ Failed to download {model_name}: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="임베딩 모델 다운로드 스크립트"
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        help="다운로드할 모델 리스트"
    )
    parser.add_argument(
        "--save-dir",
        type=str,
        default=None,
        help="모델 저장 디렉토리 (기본값: HuggingFace 캐시)"
    )

    args = parser.parse_args()

    logger.info("="*60)
    logger.info("임베딩 모델 다운로드 시작")
    logger.info("="*60)

    downloaded_models = []
    failed_models = []

    for model_name in args.models:
        try:
            result = download_model(model_name, args.save_dir)
            downloaded_models.append((model_name, result))
        except Exception as e:
            failed_models.append((model_name, str(e)))

    # 결과 출력
    logger.info("\n" + "="*60)
    logger.info("다운로드 완료")
    logger.info("="*60)

    if downloaded_models:
        logger.info(f"\n✓ 성공 ({len(downloaded_models)}개):")
        for model_name, path in downloaded_models:
            logger.info(f"  - {model_name}")
            if args.save_dir:
                logger.info(f"    → {path}")

    if failed_models:
        logger.info(f"\n✗ 실패 ({len(failed_models)}개):")
        for model_name, error in failed_models:
            logger.info(f"  - {model_name}: {error}")

    if args.save_dir:
        logger.info(f"\n모델 저장 위치: {args.save_dir}")
        logger.info("오프라인 환경에서는 이 경로를 model_name으로 사용하세요.")
    else:
        logger.info("\n모델이 HuggingFace 캐시에 저장되었습니다.")
        logger.info("오프라인 환경에서는 local_files_only=True를 사용하세요.")


if __name__ == "__main__":
    main()
