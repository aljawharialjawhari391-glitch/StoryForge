"""Application wiring for the StoryForge desktop UI bootstrap."""

from __future__ import annotations

import logging
import sys

from PySide6.QtWidgets import QApplication

from config import ConfigManager
from core import AppPaths, configure_logging
from ui.logging_handler import QtLogHandler
from ui.main_window import StoryForgeMainWindow


class StoryForgeApp:
    """Coordinates runtime dependencies and UI lifecycle."""

    def __init__(self) -> None:
        self._qt_app = QApplication(sys.argv)

        self._paths = AppPaths()
        self._config_manager = ConfigManager(self._paths)
        self._config = self._config_manager.load()
        self._logger = configure_logging(self._paths, self._config.logging)

        self._window = StoryForgeMainWindow(app_paths=self._paths, logger=self._logger)
        self._attach_ui_log_handler(self._logger, self._window)

    def run(self) -> int:
        self._window.show()
        self._logger.info("StoryForge UI bootstrap initialized.")
        return self._qt_app.exec()

    @staticmethod
    def _attach_ui_log_handler(logger: logging.Logger, window: StoryForgeMainWindow) -> None:
        ui_handler = QtLogHandler(window.log_emitter)
        ui_handler.setLevel(logging.DEBUG)
        ui_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                "%Y-%m-%d %H:%M:%S",
            )
        )
        logger.addHandler(ui_handler)
