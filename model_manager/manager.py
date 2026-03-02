"""High-level model manager scaffolding for future download/integrity workflows."""

from __future__ import annotations

from pathlib import Path

from core.paths import AppPaths
from models.model_info import ModelInfo
from model_manager.repository import ModelRepository


class ModelManager:
    """Manages known model metadata and local installation state.

    Phase 1 intentionally excludes download/install logic.
    """

    def __init__(self, app_paths: AppPaths) -> None:
        self._app_paths = app_paths
        self._repository = ModelRepository(app_paths)

    def register(self, model: ModelInfo) -> None:
        models = self._repository.read_all()
        models[model.model_id] = model
        self._repository.write_all(models)

    def list_models(self) -> list[ModelInfo]:
        models = self._repository.read_all()
        return list(models.values())

    def get(self, model_id: str) -> ModelInfo | None:
        models = self._repository.read_all()
        return models.get(model_id)

    def model_exists(self, model: ModelInfo) -> bool:
        """Return True when the model file is present in local model storage."""
        return self.model_path(model).exists()

    def model_path(self, model: ModelInfo) -> Path:
        """Return the filesystem path where a model file should exist."""
        return model.expected_path(self._app_paths.models_dir)

    def register_downloaded_model(self, model: ModelInfo) -> ModelInfo:
        """Persist model metadata after a successful download."""
        model.installed = self.model_exists(model)
        self.register(model)
        return model

    def mark_installed(self, model_id: str) -> bool:
        models = self._repository.read_all()
        model = models.get(model_id)
        if model is None:
            return False

        model_path = model.expected_path(self._app_paths.models_dir)
        model.installed = model_path.exists()
        models[model_id] = model
        self._repository.write_all(models)
        return model.installed
