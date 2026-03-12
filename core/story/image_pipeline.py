from .scene_builder import SceneBuilder


class ImagePipeline:

    def __init__(self, engine):
        self.scene_builder = SceneBuilder()
        self.engine = engine

    def generate_images(self, story: str, output_dir):

        scenes = self.scene_builder.build(story)

        results = []

        for scene in scenes:
            image_path = self.engine.generate(scene["description"], output_dir)

            results.append({
                "scene": scene["id"],
                "image": image_path
            })

        return results
