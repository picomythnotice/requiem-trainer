from src.core.handlers_base import BaseHandler


class _DummyHandler(BaseHandler):
    name = "dummy"

    def tick(self) -> None:
        pass


def test_handler_toggles():
    h = _DummyHandler()
    assert h.enabled is False
    assert h.toggle() is True
    assert h.toggle() is False
</div>