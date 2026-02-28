"""Persistence layer for model registry metadata."""

from __future__ import annotations

import json
from pathlib import Path

from core.constants import APP_MODEL_REGISTRY_FILE
from core.paths import AppPaths
from models.model_info import ModelInfo


class ModelRepository:
    """Stores and retrieves model metadata from local disk."""

    def __init__(self, app_paths: AppPaths) -> None:
        self._app_paths = app_paths
        self._app_paths.ensure()
        self._registry_path = self._app_paths.models_dir / APP_MODEL_REGISTRY_FILE

    @property
    def registry_path(self) -> Path:
        return self._registry_path

    def read_all(self) -> dict[str, ModelInfo]:
        if not self._registry_path.exists():
            return {}

        with self._registry_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        return {key: ModelInfo.from_dict(value) for key, value in payload.items()}

    def write_all(self, models: dict[str, ModelInfo]) -> None:
        serialized = {model_id: model.to_dict() for model_id, model in models.items()}
        with self._registry_path.open("w", encoding="utf-8") as handle:
            json.dump(serialized, handle, indent=2)
            handle.write("\n")
