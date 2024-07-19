import typing as tp

from error_mapper.types import _UNSET, ErrorMapType


def process_error(
    error_map: ErrorMapType,
    error: Exception,
    default: type[Exception] = _UNSET,
) -> tp.NoReturn:
    result = error_map.get(type(error))
    if result:
        raise result
    if default is not _UNSET:
        raise default from error
    raise error
