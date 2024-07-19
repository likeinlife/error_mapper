import functools
import typing as tp

from error_mapper.types import PARAM, ErrorMapType, RetType

from ._process_error import process_error


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
            process_error(error_map, e, default)

    return _wrapper
