"""Qt-aware logging bridge for sending log lines into UI widgets."""

from __future__ import annotations

import logging

from PySide6.QtCore import QObject, Signal


class LogEmitter(QObject):
    """Emits formatted log messages from Python logging into Qt slots."""

    message_ready = Signal(str)


class QtLogHandler(logging.Handler):
    """Logging handler that forwards records via a Qt signal."""

    def __init__(self, emitter: LogEmitter) -> None:
        super().__init__()
        self._emitter = emitter

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        self._emitter.message_ready.emit(message)
