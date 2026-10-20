from __future__ import annotations

import customtkinter as ctk

from src.core.engine import TrainerEngine


class TrainerOverlay(ctk.CTk):
    def __init__(self, engine: TrainerEngine) -> None:
        super().__init__()
        self.engine = engine
        self.title("Resident Evil Requiem Trainer")
        self.geometry("380x420")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")

        header = ctk.CTkLabel(self, text="REQUIEM TRAINER v0.9.3", font=("Consolas", 16, "bold"))
        header.pack(pady=(12, 8))

        for name, handler in engine.handlers.items():
            btn = ctk.CTkButton(
                self,
                text=f"[{handler.hotkey}] {name}",
                command=self._make_toggle(handler),
            )
            btn.pack(pady=4, padx=20, fill="x")

    def _make_toggle(self, handler):
        def _toggle():
            state = handler.toggle()
            print(f"{handler.name}: {'ON' if state else 'OFF'}")
        return _toggle