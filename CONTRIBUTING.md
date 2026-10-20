# Contributing to requiem-trainer

Thanks for helping improve the Resident Evil Requiem Trainer.

## Ground rules

- All contributions must target single-player / offline use only. Do not
  submit code that touches RE Net, co-op sessions, or any online service.
- Keep offsets in `src/core/offsets/` in sync with the current Steam build.
  Bump `offsets/BUILD_ID` whenever you regenerate them.
- Do not commit prebuilt binaries or memory dumps.
- Follow the existing handler pattern: every feature lives in
  `src/handlers/` and registers itself via `register_handler()`.

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.bootstrap
```

## Pull requests

- One feature per PR.
- Include a stub test under `tests/` if you touch the engine or offset resolver.
- Run `pytest -q` before opening.

## Reporting offset drift

Open an issue with the game build number, your trainer log, and the AOB
signature that failed. Logs live under `logs/trainer.log`.