Read ARCHITECTURE.md and ROADMAP.md carefully.

Implement Phase 3 – Automatic Model Download System.

Requirements:

1. Extend ModelManager to support:
   - Checking if a model file exists in the models directory.
   - Registering a model after download.
2. Implement a ModelDownloader module:
   - Download model from a given URL.
   - Show progress in logs.
   - Save model file to models directory.
3. On application startup:
   - Automatically check if base image model exists.
   - If not, trigger download automatically.
4. Use a lightweight Stable Diffusion 1.5 optimized checkpoint (~2GB).
5. Ensure Windows compatibility.
6. Keep modular architecture.
7. Do NOT implement image generation yet.
8. Production-ready clean code.
9. Return structured commits.

Goal:
Enable automatic AI model preparation at startup.
