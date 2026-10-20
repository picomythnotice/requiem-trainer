from __future__ import annotations

from src.core.handlers_base import BaseHandler


class InventoryUnlockHandler(BaseHandler):
    name = "inventory_unlock"
    hotkey = "F5"

    def tick(self) -> None:
        engine = self._engine
        if not engine or engine.memory is None:
            return
        base = engine.memory.base_module() + engine.resolver["player_base"]
        slot_addr = base + engine.resolver["inventory_slot"]
        # set every slot to 'unlocked'
        for i in range(24):
            engine.memory.write_bytes(slot_addr + i * 4, b"\x01\x00\x00\x00")