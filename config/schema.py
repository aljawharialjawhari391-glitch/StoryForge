"""Configuration schemas for StoryForge foundation settings."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class LoggingConfig:
    level: str = "INFO"
    console_enabled: bool = True
    max_bytes: int = 1_000_000
    backup_count: int = 5


@dataclass(slots=True)
class PathsConfig:
    models_subdir: str = "models"
    cache_subdir: str = "cache"


@dataclass(slots=True)
class AppConfig:
    environment: str = "production"
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    paths: PathsConfig = field(default_factory=PathsConfig)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "AppConfig":
        logging_payload = payload.get("logging", {})
        paths_payload = payload.get("paths", {})
        return cls(
            environment=payload.get("environment", "production"),
            logging=LoggingConfig(
                level=logging_payload.get("level", "INFO"),
                console_enabled=logging_payload.get("console_enabled", True),
                max_bytes=logging_payload.get("max_bytes", 1_000_000),
                backup_count=logging_payload.get("backup_count", 5),
            ),
            paths=PathsConfig(
                models_subdir=paths_payload.get("models_subdir", "models"),
                cache_subdir=paths_payload.get("cache_subdir", "cache"),
            ),
        )
