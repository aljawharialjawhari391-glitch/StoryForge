"""Windows-friendly path management for StoryForge."""

from __future__ import annotations

import os
import platform
from pathlib import Path

from core.constants import APP_NAME


def _resolve_windows_data_root() -> Path:
    """Resolve a writable app-data directory on Windows with fallbacks."""
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata)

    local_app_data = os.getenv("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data)

    return Path.home() / "AppData" / "Roaming"


def _resolve_non_windows_data_root() -> Path:
    """Resolve a writable app-data directory for non-Windows systems."""
    xdg_data_home = os.getenv("XDG_DATA_HOME")
    if xdg_data_home:
        return Path(xdg_data_home)

    return Path.home() / ".local" / "share"


class AppPaths:
    """Builds and creates canonical application folders used by all subsystems."""

    def __init__(self, app_name: str = APP_NAME) -> None:
        self.app_name = app_name

    @property
    def data_root(self) -> Path:
        if platform.system().lower().startswith("win"):
            return _resolve_windows_data_root() / self.app_name

        return _resolve_non_windows_data_root() / self.app_name.lower()

    @property
    def config_dir(self) -> Path:
        return self.data_root / "config"

    @property
    def logs_dir(self) -> Path:
        return self.data_root / "logs"

    @property
    def models_dir(self) -> Path:
        return self.data_root / "models"

    @property
    def cache_dir(self) -> Path:
        return self.data_root / "cache"

    def ensure(self) -> None:
        """Create required directories if they are missing."""
        for path in (
            self.data_root,
            self.config_dir,
            self.logs_dir,
            self.models_dir,
            self.cache_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)
