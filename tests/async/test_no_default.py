from typing import TYPE_CHECKING

import pytest
from error_mapper import ErrorMapTypeExecute, on_error_execute
from error_mapper.error_map._decorator import error_map_decorator

if TYPE_CHECKING:
    from error_mapper.types import ErrorMapType


async def test_async_on_error_execute_unexpected():
    error_map: ErrorMapTypeExecute = {}

    class UnexpectedError(Exception): ...

    @on_error_execute(error_map)
    async def fn() -> None:
        raise UnexpectedError

    with pytest.raises(UnexpectedError):
        await fn()


async def test_async_error_mapping_unexpected():
    error_map: ErrorMapType = {}

    class UnexpectedError(Exception): ...

    @error_map_decorator(error_map)
    async def fn() -> None:
        raise UnexpectedError

    with pytest.raises(UnexpectedError):
        await fn()
