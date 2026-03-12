from __future__ import annotations


class StoryEngine:
    """
    Converts a story description into cinematic scenes.
    """

    def generate_scenes(self, story: str) -> list[str]:
        story = story.strip()

        if not story:
            return []

        sentences = story.split(".")

        scenes = []

        for sentence in sentences:
            sentence = sentence.strip()

            if sentence:
                scenes.append(sentence)

        return scenes
