from __future__ import annotations

import time
from typing import Callable

from loguru import logger

from src.core.memory import ProcessMemory
from src.core.offsets.resolver import OffsetResolver
from src.core.handlers_base import BaseHandler


class TrainerEngine:
    """Owns the process handle, offset resolver, and active handlers."""

    def __init__(self, process_name: str, resolver: OffsetResolver) -> None:
        self.process_name = process_name
        self.resolver = resolver
        self.memory: ProcessMemory | None = None
        self.handlers: dict[str, BaseHandler] = {}
        self._running = False

    def attach(self) -> bool:
        try:
            self.memory = ProcessMemory.attach(self.process_name)
            logger.success("attached pid={}", self.memory.pid)
            return True
        except Exception as exc:  # noqa: BLE001
            logger.error("attach failed: {}", exc)
            return False

    def register(self, handler: BaseHandler) -> None:
        self.handlers[handler.name] = handler
        handler.bind(self)
        logger.debug("registered handler: {}", handler.name)

    def run_loop(self, tick: float = 0.05) -> None:
        self._running = True
        try:
            while self._running:
                for handler in self.handlers.values():
                    if handler.enabled:
                        handler.tick()
                time.sleep(tick)
        except KeyboardInterrupt:
            logger.info("shutdown requested")
        finally:
            self._running = False

    def stop(self) -> None:
        self._running = False