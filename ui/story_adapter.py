from core.story.story_controller import StoryController


class StoryAdapter:

    def __init__(self, engine):
        self.controller = StoryController(engine)

    def generate(self, story):
        return self.controller.generate_story_images(story)
