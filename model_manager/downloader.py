"""Model downloading utilities for startup model provisioning."""

from __future__ import annotations

import logging
import tempfile
import urllib.request
from pathlib import Path


class ModelDownloadError(RuntimeError):
    """Raised when a model download fails."""


class ModelDownloader:
    """Downloads model files with progressive logging output."""

    _BUFFER_SIZE = 1024 * 1024

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def download(self, url: str, destination: Path) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        self._logger.info("Starting model download: %s", url)

        temp_handle = tempfile.NamedTemporaryFile(
            mode="wb",
            delete=False,
            dir=str(destination.parent),
            prefix=f"{destination.name}.",
            suffix=".tmp",
        )
        temp_path = Path(temp_handle.name)

        try:
            with temp_handle, urllib.request.urlopen(url) as response:
                total_size = int(response.headers.get("Content-Length", "0"))
                downloaded_bytes = 0
                next_log_threshold = 5

                while True:
                    chunk = response.read(self._BUFFER_SIZE)
                    if not chunk:
                        break

                    temp_handle.write(chunk)
                    downloaded_bytes += len(chunk)

                    progress = self._calculate_progress(downloaded_bytes, total_size)
                    if progress >= next_log_threshold:
                        self._logger.info(
                            "Model download progress: %s%% (%s/%s)",
                            progress,
                            self._format_size(downloaded_bytes),
                            self._format_size(total_size) if total_size else "unknown",
                        )
                        next_log_threshold += 5

            temp_path.replace(destination)
            self._logger.info("Model download completed: %s", destination)
            return destination
        except Exception as exc:  # noqa: BLE001 - convert to domain exception
            if temp_path.exists():
                temp_path.unlink(missing_ok=True)
            raise ModelDownloadError(f"Failed downloading model from {url}: {exc}") from exc

    @staticmethod
    def _calculate_progress(downloaded: int, total: int) -> int:
        if total <= 0:
            return 0

        return min(100, int((downloaded / total) * 100))

    @staticmethod
    def _format_size(num_bytes: int) -> str:
        if num_bytes <= 0:
            return "0 B"

        units = ["B", "KB", "MB", "GB", "TB"]
        size = float(num_bytes)
        for unit in units:
            if size < 1024 or unit == units[-1]:
                return f"{size:.1f} {unit}"
            size /= 1024

        return f"{size:.1f} TB"
