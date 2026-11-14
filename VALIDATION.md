# Publication verification

Checked 14 November 2026 on Windows using a fresh Python 3.13 environment and Node.js 24. This is a local functional check, not deployment certification or detection-accuracy evaluation.

## Automated checks

- Clean `npm ci` installation and production TypeScript/Vite build passed.
- Fresh installation from `requirements-lock.txt` succeeded; `pip check` reported no broken requirements.
- Python suite: **32 passed**. Covers event progression without duplicate alerts, stored review decisions, timed movement rules, invalid inputs, uploads, independent aisle lighting, journey transitions, safe fallback and energy timing.
- JavaScript savings suite: **4 passed**.
- Cached pose model passed the setup script's SHA-256 verification.

The build reports a large JavaScript bundle advisory (about 1.19 MB before compression). The Python test client reports an upstream HTTPX deprecation warning. Neither prevented the checked workflows. The setup script's dependency/build stages were exercised individually; its model download was verified against the existing official model cache, not a second download.

## Actual browser checks

- Business overview and security workspace opened from the clean build.
- Multi-shopper scene ran at 2×, reached level 3 and produced one upgraded scripted event. Its source and lack of real video evidence were labelled.
- **Analyse recorded sample** completed local MediaPipe inference on the credited ordinary-shopping clip. A real neutral zone-entry observation was created automatically, with a playable **6.08-second** evidence clip.
- A review decision and note were saved through the UI and remained visible after browser refresh.
- One customer in A2 produced **30% / 100% / 30%** aisle brightness. The owner cards showed **69W**, **24.84kWh/month** and **LKR 7,452/month** at the dummy LKR 300/kWh price.
- The 3D scene rendered; the full-screen control expanded only the simulation and returned to the workspace.
- Animated lighting flow advanced from step 1 to step 5. The separate circuit view showed A1 at 30% and selected A2 at 100% with one person present.
- No browser console errors were reported during these checks.

## Publication boundaries

Only source, documentation, selected dependency notices, a synthetic-scene screenshot and the credited development sample are published. Prior environments, backups, databases, user uploads, generated review clips, logs, model binaries and build output are excluded. The source clone supplied by the team is left unchanged.

These checks do not establish theft/concealment accuracy, real energy savings, live CCTV integration, production access control, electrical safety or other-platform compatibility. The included sample is development footage; there is no independent held-out concealment benchmark. Setup needs internet; the prepared local demo uses cached assets.
