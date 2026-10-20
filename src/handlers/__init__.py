from __future__ import annotations

from src.handlers.godmode import GodmodeHandler
from src.handlers.infinite_ammo import InfiniteAmmoHandler
from src.handlers.money_editor import MoneyEditorHandler
from src.handlers.speed_hack import SpeedHackHandler
from src.handlers.inventory_unlock import InventoryUnlockHandler


def load_all_handlers(engine) -> None:
    for handler_cls in (
        GodmodeHandler,
        InfiniteAmmoHandler,
        MoneyEditorHandler,
        SpeedHackHandler,
        InventoryUnlockHandler,
    ):
        engine.register(handler_cls())