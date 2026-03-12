from .story_engine import StoryEngine


class SceneBuilder:

    def __init__(self):
        self.engine = StoryEngine()

    def build(self, story: str):

        scenes = self.engine.generate_scenes(story)

        structured = []

        for i, scene in enumerate(scenes):
            structured.append({
                "id": i + 1,
                "description": scene
            })

        return structured
