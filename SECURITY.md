# Security Policy

## Supported scope

The Resident Evil Requiem Trainer is a **single-player, offline-only memory
trainer**. It is intended for personal use with a legitimately owned copy of
the game running in offline mode.

## Out of scope

- Online / co-op sessions
- Anti-cheat interaction
- Distribution of game assets

## Reporting a vulnerability

If you discover a vulnerability in the trainer itself (privilege escalation
via the injector, unsafe YAML deserialization, DLL search order hijack in the
overlay, etc.), open a private security advisory on GitHub or email
`security@requiem-trainer.dev`.

Please include:
- Trainer version / commit hash
- Steps to reproduce
- Impact assessment

We aim to acknowledge within 72 hours.

## Warning

Use at your own risk. Running any memory trainer against a game may violate
the game's EULA. Do not use this while the game is connected to online
services.