from __future__ import annotations

from src.core.handlers_base import BaseHandler


class SpeedHackHandler(BaseHandler):
    name = "speed_hack"
    hotkey = "F4"
    multiplier: float = 2.0

    def tick(self) -> None:
        engine = self._engine
        if not engine or engine.memory is None:
            return
        base = engine.memory.base_module() + engine.resolver["player_base"]
        # walk the speed pointer chain (base + 0x120 -> +0x8)
        ptr = engine.memory.read_int(base + 0x120)
        if ptr:
            engine.memory.write_float(ptr + 0x8, 6.0 * self.multiplier)