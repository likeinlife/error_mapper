import typing as tp

from error_mapper.types import _UNSET, ErrorMapTypeExecute


def process_error(
    execute_map: ErrorMapTypeExecute,
    error: Exception,
    default: type[Exception] = _UNSET,
) -> tp.NoReturn:
    result = execute_map.get(type(error))
    if result:
        result(error)
    if default is not _UNSET:
        raise default from error
    raise error
