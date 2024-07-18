import functools
import typing as tp

from error_mapper.types import PARAM, ErrorMapTypeExecute, RetType


def sync_wrapper(
    func: tp.Callable[PARAM, RetType],
    execute_map: ErrorMapTypeExecute,
    default: type[Exception],
) -> tp.Callable[PARAM, RetType]:
    @functools.wraps(func)
    def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            result = execute_map.get(type(e))
            if not result:
                raise default from e
            result(e)

    return _wrapper
