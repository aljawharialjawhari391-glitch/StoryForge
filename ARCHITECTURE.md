# StoryForge Architecture (Windows – SD 1.5)

## System Overview

StoryForge is a fully offline AI desktop video generation engine built for Windows.

Core Goals:
- Generate 8-minute AI cinematic videos
- Support multiple visual styles (Realistic, Cartoon, Fantasy, etc.)
- Automatic model download & management
- Lip Sync support
- Scene-based animation
- Production-ready architecture
- Future commercial readiness

---

## System Layers

### 1. Story Intelligence Layer
- Scene splitter
- Emotion detection
- Character extraction
- Narrative structure analysis

### 2. Style Engine
- Preset-based style system
- LoRA routing per style
- Lighting & color grading profiles
- Automatic model selection

### 3. Model Manager
- Automatic model download
- Version control
- Integrity verification
- Local model storage organization
- Windows-compatible paths

### 4. Image Generation Engine
- Stable Diffusion 1.5 integration
- Character consistency system
- Seed locking
- Batch scene rendering

### 5. Animation Engine
- AnimateDiff integration
- Motion intensity control
- Camera movement system
- Scene transitions

### 6. Lip Sync Engine
- Wav2Lip integration
- Face detection
- Audio alignment system

### 7. Audio Engine
- Coqui TTS integration
- Voice profile selection
- Emotion-aware voice rendering

### 8. Render Engine
- FFmpeg orchestration
- Multi aspect ratio support:
  - 9:16
  - 16:9
  - 1:1
  - 4:5
- Quality presets (Low / Medium / High)

### 9. Desktop Application Layer
- Built with PySide6
- Style selector
- Resolution selector
- Timeline progress display
- Project save/load system
- Export manager
- Settings manager

---

## Project Philosophy

- Modular architecture
- Expandable engine
- GPU-optimized pipeline
- Offline-first design
- Ready for future licensing system
