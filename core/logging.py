"""Centralized logging bootstrap for StoryForge."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from config.schema import LoggingConfig
from core.constants import APP_LOG_FILE
from core.paths import AppPaths


def configure_logging(app_paths: AppPaths, logging_config: LoggingConfig) -> logging.Logger:
    """Configure file and console loggers for the application runtime."""
    app_paths.ensure()
    log_file = app_paths.logs_dir / APP_LOG_FILE

    logger = logging.getLogger("storyforge")
    logger.setLevel(getattr(logging, logging_config.level.upper(), logging.INFO))
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    logger.handlers.clear()

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=logging_config.max_bytes,
        backupCount=logging_config.backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if logging_config.console_enabled:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
