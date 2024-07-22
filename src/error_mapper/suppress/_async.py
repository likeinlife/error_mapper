import functools
import typing as tp

from error_mapper.types import PARAM, RetType


def async_wrapper(
    exception: type[Exception],
    func: tp.Callable[PARAM, tp.Awaitable[RetType]],
) -> tp.Callable[PARAM, tp.Awaitable[RetType | None]]:
    @functools.wraps(func)
    async def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType | None:
        try:
            return await func(*args, **kwargs)
        except exception:
            return None

    return _wrapper
