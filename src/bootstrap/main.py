from __future__ import annotations

import sys
import yaml
from pathlib import Path

from loguru import logger

from src.core.engine import TrainerEngine
from src.core.offsets.resolver import OffsetResolver
from src.handlers import load_all_handlers


def _load_config(path: Path) -> dict:
    if not path.exists():
        logger.warning("config missing at {}, using defaults", path)
        return {"process_name": "re_requiem.exe", "auto_attach": True}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    config_path = Path("config/trainer.yaml")
    cfg = _load_config(config_path)

    logger.add("logs/trainer.log", rotation="2 MB", retention="5 days")

    resolver = OffsetResolver.from_build(cfg.get("build_id", "0.0.0"))
    engine = TrainerEngine(
        process_name=cfg.get("process_name", "re_requiem.exe"),
        resolver=resolver,
    )

    load_all_handlers(engine)

    if cfg.get("auto_attach", True):
        if not engine.attach():
            logger.error("could not attach to {}", cfg.get("process_name"))
            return 1

    logger.info("trainer ready — {} handlers registered", len(engine.handlers))
    engine.run_loop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())