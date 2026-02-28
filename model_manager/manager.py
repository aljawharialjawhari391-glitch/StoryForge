"""High-level model manager scaffolding for future download/integrity workflows."""

from __future__ import annotations

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
