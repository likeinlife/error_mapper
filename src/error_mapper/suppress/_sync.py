import functools
import typing as tp

from error_mapper.types import PARAM, RetType


def sync_wrapper(
    exception: type[Exception],
    func: tp.Callable[PARAM, RetType],
) -> tp.Callable[PARAM, RetType | None]:
    @functools.wraps(func)
    def _wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> RetType | None:
        try:
            return func(*args, **kwargs)
        except exception:
            return None

    return _wrapper
