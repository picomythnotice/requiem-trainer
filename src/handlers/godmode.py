from __future__ import annotations

from src.core.handlers_base import BaseHandler


class GodmodeHandler(BaseHandler):
    name = "godmode"
    hotkey = "F1"

    def tick(self) -> None:
        engine = self._engine
        if not engine or engine.memory is None:
            return
        base = engine.memory.base_module() + engine.resolver["player_base"]
        hp_addr = base + engine.resolver["health"]
        engine.memory.write_int(hp_addr, 9999)