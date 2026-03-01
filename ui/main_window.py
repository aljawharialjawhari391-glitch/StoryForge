"""Main window implementation for StoryForge Phase 2 UI bootstrap."""

from __future__ import annotations

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from core.paths import AppPaths
from model_manager import ModelManager
from ui.logging_handler import LogEmitter


class StoryForgeMainWindow(QMainWindow):
    """Primary application window with bootstrap-level controls."""

    def __init__(self, app_paths: AppPaths, logger: logging.Logger) -> None:
        super().__init__()
        self._app_paths = app_paths
        self._logger = logger
        self._model_manager: ModelManager | None = None

        self.setWindowTitle("StoryForge")
        self.resize(900, 560)

        self._log_emitter = LogEmitter()
        self._build_ui()
        self._wire_signals()

    @property
    def log_emitter(self) -> LogEmitter:
        return self._log_emitter

    def _build_ui(self) -> None:
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(18, 18, 18, 18)
        root_layout.setSpacing(12)
        central_widget.setLayout(root_layout)

        title_label = QLabel("StoryForge")
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title_label.setObjectName("appTitle")
        title_label.setStyleSheet("font-size: 28px; font-weight: 600;")

        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(10)

        self._status_label = QLabel("Engine status: Idle")
        self._status_label.setObjectName("statusLabel")

        self._test_model_manager_button = QPushButton("Test Model Manager")
        self._test_model_manager_button.setObjectName("testModelManagerButton")

        controls_layout.addWidget(self._status_label)
        controls_layout.addStretch(1)
        controls_layout.addWidget(self._test_model_manager_button)

        self._log_output = QTextEdit()
        self._log_output.setReadOnly(True)
        self._log_output.setPlaceholderText("Runtime logs will appear here...")
        self._log_output.setObjectName("logOutput")

        root_layout.addWidget(title_label)
        root_layout.addLayout(controls_layout)
        root_layout.addWidget(self._log_output, stretch=1)

    def _wire_signals(self) -> None:
        self._test_model_manager_button.clicked.connect(self._on_test_model_manager_clicked)
        self._log_emitter.message_ready.connect(self._append_log_message)

    def _on_test_model_manager_clicked(self) -> None:
        self._status_label.setText("Engine status: Initializing model manager...")
        self._model_manager = ModelManager(self._app_paths)

        model_count = len(self._model_manager.list_models())
        self._status_label.setText(f"Engine status: Model manager ready ({model_count} models)")
        self._logger.info("Model manager initialized from UI action. Registered models: %d", model_count)

    def _append_log_message(self, message: str) -> None:
        self._log_output.append(message)
