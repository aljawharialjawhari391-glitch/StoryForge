"""StoryForge Phase 2 desktop bootstrap entry point."""

from __future__ import annotations

import sys

from ui import StoryForgeApp


def main() -> int:
    app = StoryForgeApp()
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())
