"""Model metadata entities used by the model manager."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ModelInfo:
    model_id: str
    name: str
    version: str
    file_name: str
    installed: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ModelInfo":
        return cls(
            model_id=payload["model_id"],
            name=payload["name"],
            version=payload["version"],
            file_name=payload["file_name"],
            installed=payload.get("installed", False),
        )

    def expected_path(self, models_dir: Path) -> Path:
        return models_dir / self.file_name
