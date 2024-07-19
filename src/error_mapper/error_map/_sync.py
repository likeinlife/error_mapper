import functools
import typing as tp

from error_mapper.types import _UNSET, PARAM, ErrorMapType, RetType

from ._process_error import process_error


def sync_wrapper(
    func: tp.Callable[PARAM, RetType],
    error_map: ErrorMapType,
    default: type[Exception] = _UNSET,
) -> tp.Callable[PARAM, RetType]:
    @functools.wraps(func)
    def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            process_error(error_map, e, default)

    return _wrapper
