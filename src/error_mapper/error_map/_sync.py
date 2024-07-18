import functools
import typing as tp

from error_mapper.types import PARAM, ErrorMapType, RetType


def sync_wrapper(
    func: tp.Callable[PARAM, RetType],
    error_map: ErrorMapType,
    default: type[Exception],
) -> tp.Callable[PARAM, RetType]:
    @functools.wraps(func)
    def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise error_map.get(type(e), default) from e

    return _wrapper
