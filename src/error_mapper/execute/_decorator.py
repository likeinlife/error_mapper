import asyncio
import typing as tp

from error_mapper.types import _UNSET, PARAM, ErrorMapTypeExecute, FuncType, RetType

from ._async import async_wrapper
from ._sync import sync_wrapper


def on_error_execute(
    error_map: ErrorMapTypeExecute,
    default: type[Exception] = _UNSET,
) -> tp.Callable[[FuncType[PARAM, RetType]], FuncType[PARAM, RetType]]:
    """Map function on errors.

    If no mapping found, raise default exception.
    """

    def decorator(fn: FuncType[PARAM, RetType]) -> FuncType[PARAM, RetType]:
        if asyncio.iscoroutinefunction(fn):
            return tp.cast(FuncType[PARAM, RetType], async_wrapper(fn, error_map, default))
        return sync_wrapper(fn, error_map, default)

    return decorator
