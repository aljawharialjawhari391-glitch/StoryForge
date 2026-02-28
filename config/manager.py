"""Configuration management: loading, validating and persisting app settings."""

from __future__ import annotations

import json
from pathlib import Path

from config.schema import AppConfig
from core.constants import APP_CONFIG_FILE
from core.paths import AppPaths


class ConfigManager:
    """Read and write StoryForge configuration with sane defaults."""

    def __init__(self, app_paths: AppPaths) -> None:
        self._app_paths = app_paths
        self._app_paths.ensure()
        self._config_path = self._app_paths.config_dir / APP_CONFIG_FILE

    @property
    def config_path(self) -> Path:
        return self._config_path

    def load(self) -> AppConfig:
        if not self._config_path.exists():
            config = AppConfig()
            self.save(config)
            return config

        with self._config_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        return AppConfig.from_dict(payload)

    def save(self, config: AppConfig) -> None:
        with self._config_path.open("w", encoding="utf-8") as handle:
            json.dump(config.to_dict(), handle, indent=2)
            handle.write("\n")
