from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Pattern:
    signature: str

    def to_bytes(self) -> bytes:
        return bytes(int(b, 16) for b in self.signature.split() if b != "??")


def find_pattern(memory, base: int, size: int, pattern: Pattern) -> int | None:
    needle = pattern.to_bytes()
    chunk = memory._pm.read_bytes(base, size)
    idx = chunk.find(needle)
    return base + idx if idx >= 0 else None