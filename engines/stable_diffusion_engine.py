import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path
import datetime


class StableDiffusionEngine:
    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.pipe = None

    def load(self):
        self.pipe = StableDiffusionPipeline.from_single_file(
            str(self.model_path),
            torch_dtype=torch.float32,
        )
        self.pipe = self.pipe.to("cpu")

    def generate(self, prompt: str, output_dir: Path):
        if self.pipe is None:
            raise RuntimeError("Engine not loaded")

        image = self.pipe(prompt, num_inference_steps=20).images[0]

        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = output_dir / f"image_{timestamp}.png"

        image.save(output_path)

        return output_path
