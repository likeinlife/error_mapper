from error_mapper import suppress_to_none_async

from tests.mocks import RaiseError


async def test_async_suppress_error():
    @suppress_to_none_async(RaiseError)
    async def fn() -> int:
        raise RaiseError

    assert await fn() is None


async def test_async_suppress_no_error():
    @suppress_to_none_async(RaiseError)
    async def fn() -> int:
        return 1

    assert await fn() == 1
