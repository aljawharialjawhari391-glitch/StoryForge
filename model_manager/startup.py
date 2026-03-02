"""Startup provisioning workflow for required AI models."""

from __future__ import annotations

import logging

from core.paths import AppPaths
from model_manager.catalog import BASE_IMAGE_MODEL
from model_manager.downloader import ModelDownloadError, ModelDownloader
from model_manager.manager import ModelManager


class StartupModelProvisioner:
    """Ensures required base models are available before runtime workloads start."""

    def __init__(self, app_paths: AppPaths, logger: logging.Logger) -> None:
        self._logger = logger
        self._manager = ModelManager(app_paths)
        self._downloader = ModelDownloader(logger)

    def ensure_base_model(self) -> None:
        model = BASE_IMAGE_MODEL

        if self._manager.model_exists(model):
            self._manager.register_downloaded_model(model)
            self._logger.info("Base image model already present: %s", model.file_name)
            return

        if not model.source_url:
            self._logger.error("Base image model URL is missing; cannot auto-download.")
            return

        self._logger.info("Base image model missing. Triggering automatic download.")
        destination = self._manager.model_path(model)

        try:
            self._downloader.download(model.source_url, destination)
            self._manager.register_downloaded_model(model)
            self._logger.info("Base image model registered successfully.")
        except ModelDownloadError as exc:
            self._logger.exception("Automatic base model provisioning failed: %s", exc)
