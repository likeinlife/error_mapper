import typing as tp

from error_mapper.protocols import OnErrorExecuteFunction

PARAM = tp.ParamSpec("PARAM")
RetType = tp.TypeVar("RetType")

ErrorMapType: tp.TypeAlias = dict[type[Exception], type[Exception]]
ErrorMapTypeExecute: tp.TypeAlias = dict[type[Exception], OnErrorExecuteFunction]
FuncType: tp.TypeAlias = tp.Callable[PARAM, RetType]

_UNSET: tp.Any = object()
