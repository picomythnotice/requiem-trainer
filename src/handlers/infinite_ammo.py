from __future__ import annotations

from src.core.handlers_base import BaseHandler


class InfiniteAmmoHandler(BaseHandler):
    name = "infinite_ammo"
    hotkey = "F2"

    def tick(self) -> None:
        engine = self._engine
        if not engine or engine.memory is None:
            return
        base = engine.memory.base_module() + engine.resolver["player_base"]
        ammo_addr = base + engine.resolver["ammo"]
        engine.memory.write_int(ammo_addr, 999)