from src.core.offsets.resolver import OffsetResolver


def test_resolver_known_build():
    r = OffsetResolver.from_build("1.0.4.0")
    assert r["health"] == 0x150
    assert r["ammo"] == 0x2B8


def test_resolver_falls_back_to_latest():
    r = OffsetResolver.from_build("9.9.9.9")
    assert r.table.build_id == "1.0.4.0"
    assert r["player_base"] == 0x0A412E88