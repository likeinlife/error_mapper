import typing as tp

from error_mapper.types import PARAM, FuncType, RetType

from ._async import async_wrapper
from ._sync import sync_wrapper


def suppress_to_none(
    exception: type[Exception],
) -> tp.Callable[[FuncType[PARAM, RetType]], FuncType[PARAM, RetType | None]]:
    """Suppress error and return None instead."""

    def decorator(fn: FuncType[PARAM, RetType]) -> FuncType[PARAM, RetType | None]:
        return sync_wrapper(exception, fn)

    return decorator


def suppress_to_none_async(
    exception: type[Exception],
) -> tp.Callable[[FuncType[PARAM, tp.Awaitable[RetType]]], FuncType[PARAM, tp.Awaitable[RetType | None]]]:
    """Suppress error and return None instead."""

    def decorator(fn: FuncType[PARAM, tp.Awaitable[RetType]]) -> FuncType[PARAM, tp.Awaitable[RetType | None]]:
        return async_wrapper(exception, fn)

    return decorator
