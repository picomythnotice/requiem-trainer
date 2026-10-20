from __future__ import annotations

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """Every trainer feature (godmode, infinite ammo, etc.) subclasses this."""

    name: str = "base"
    hotkey: str | None = None

    def __init__(self) -> None:
        self.enabled: bool = False
        self._engine = None

    def bind(self, engine) -> None:
        self._engine = engine

    def toggle(self) -> bool:
        self.enabled = not self.enabled
        return self.enabled

    @abstractmethod
    def tick(self) -> None:
        """Called each engine loop iteration while enabled."""