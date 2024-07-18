import functools
import typing as tp

from error_mapper.types import PARAM, ErrorMapType, RetType


def async_wrapper(
    func: tp.Callable[PARAM, tp.Awaitable[RetType]],
    error_map: ErrorMapType,
    default: type[Exception],
) -> tp.Callable[PARAM, tp.Awaitable[RetType]]:
    @functools.wraps(func)
    async def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            raise error_map.get(type(e), default) from e

    return _wrapper
