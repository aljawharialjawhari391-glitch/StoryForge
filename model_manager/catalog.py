"""Model catalog entries used for startup provisioning."""

from __future__ import annotations

from models.model_info import ModelInfo

BASE_IMAGE_MODEL = ModelInfo(
    model_id="sd15-base",
    name="Stable Diffusion v1.5 (Pruned EMA)",
    version="1.5",
    file_name="v1-5-pruned-emaonly.safetensors",
    source_url=(
        "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/"
        "v1-5-pruned-emaonly.safetensors"
    ),
)
