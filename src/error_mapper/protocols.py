import typing as tp


class OnErrorExecuteFunction(tp.Protocol):
    def __call__(self, error: Exception) -> tp.NoReturn: ...
