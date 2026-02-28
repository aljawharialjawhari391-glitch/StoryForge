"""StoryForge Phase 1 bootstrap entry point."""

from __future__ import annotations

from config import ConfigManager
from core import AppPaths, configure_logging
from model_manager import ModelManager


def bootstrap() -> None:
    paths = AppPaths()
    config_manager = ConfigManager(paths)
    config = config_manager.load()

    logger = configure_logging(paths, config.logging)
    logger.info("StoryForge foundation initialized.")

    model_manager = ModelManager(paths)
    logger.info("Model manager ready with %d registered models.", len(model_manager.list_models()))


if __name__ == "__main__":
    bootstrap()
