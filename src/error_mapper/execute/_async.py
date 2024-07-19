import functools
import typing as tp

from error_mapper.types import _UNSET, PARAM, ErrorMapTypeExecute, RetType


def async_wrapper(
    func: tp.Callable[PARAM, tp.Awaitable[RetType]],
    execute_map: ErrorMapTypeExecute,
    default: type[Exception] = _UNSET,
) -> tp.Callable[PARAM, tp.Awaitable[RetType]]:
    @functools.wraps(func)
    async def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            result = execute_map.get(type(e))
            if result:
                result(e)
            if default is not _UNSET:
                raise default from e
            raise e from e

    return _wrapper
