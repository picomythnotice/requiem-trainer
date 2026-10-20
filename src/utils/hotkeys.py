from __future__ import annotations

import keyboard
from loguru import logger

from src.core.engine import TrainerEngine


def bind_hotkeys(engine: TrainerEngine) -> None:
    for name, handler in engine.handlers.items():
        if not handler.hotkey:
            continue
        keyboard.add_hotkey(handler.hotkey, _toggle(handler))
        logger.debug("bound {} -> {}", handler.hotkey, name)


def _toggle(handler):
    def _fn() -> None:
        state = handler.toggle()
        logger.info("{} -> {}", handler.name, "ON" if state else "OFF")
    return _fn