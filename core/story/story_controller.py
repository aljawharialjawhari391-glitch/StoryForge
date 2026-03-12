from pathlib import Path
from .image_pipeline import ImagePipeline


class StoryController:

    def __init__(self, engine):
        self.pipeline = ImagePipeline(engine)

    def generate_story_images(self, story: str):

        output_dir = Path("outputs")

        return self.pipeline.generate_images(story, output_dir)
