from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class OffsetTable:
    build_id: str
    player_base: int
    health: int
    ammo: int
    money: int
    inventory_slot: int
    extra: dict[str, int] = field(default_factory=dict)


# Populated by tools/dump_offsets.py against a live process.
_KNOWN_TABLES: dict[str, OffsetTable] = {
    "1.0.2.0": OffsetTable(
        build_id="1.0.2.0",
        player_base=0x0A3F2C10,
        health=0x148,
        ammo=0x2B0,
        money=0x3C8,
        inventory_slot=0x410,
    ),
    "1.0.4.0": OffsetTable(
        build_id="1.0.4.0",
        player_base=0x0A412E88,
        health=0x150,
        ammo=0x2B8,
        money=0x3D0,
        inventory_slot=0x418,
    ),
}


class OffsetResolver:
    def __init__(self, table: OffsetTable) -> None:
        self.table = table

    @classmethod
    def from_build(cls, build_id: str) -> "OffsetResolver":
        table = _KNOWN_TABLES.get(build_id)
        if table is None:
            # fall back to newest known table
            table = max(_KNOWN_TABLES.values(), key=lambda t: t.build_id)
        return cls(table)

    def __getitem__(self, key: str) -> int:
        return getattr(self.table, key)