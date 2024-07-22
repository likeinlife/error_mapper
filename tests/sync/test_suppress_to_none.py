from error_mapper import suppress_to_none

from tests.mocks import RaiseError


def test_suppress_error():
    @suppress_to_none(RaiseError)
    def fn() -> int:
        raise RaiseError

    assert fn() is None


def test_suppress_no_error():
    @suppress_to_none(RaiseError)
    def fn() -> int:
        return 1

    assert fn() == 1
