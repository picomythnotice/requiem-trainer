from __future__ import annotations

from src.core.handlers_base import BaseHandler


class MoneyEditorHandler(BaseHandler):
    name = "money_editor"
    hotkey = "F3"
    target_value: int = 999_999

    def tick(self) -> None:
        engine = self._engine
        if not engine or engine.memory is None:
            return
        base = engine.memory.base_module() + engine.resolver["player_base"]
        money_addr = base + engine.resolver["money"]
        engine.memory.write_int(money_addr, self.target_value)