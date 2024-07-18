import pytest
from error_mapper import ErrorMapType, error_map_decorator

from .mocks import (
    DefaultError,
    Raise1Error,
    Raise2Error,
    Raise3Error,
    RaiseError,
    Suppressed1Error,
    Suppressed2Error,
    Suppressed3Error,
    SuppressedError,
)


def test_on_error_execute_unexpected():
    error_map: ErrorMapType = {}

    @error_map_decorator(error_map, DefaultError)
    def fn() -> None:
        raise ValueError

    with pytest.raises(DefaultError):
        fn()


def test_error_map_decorator():
    error_map: ErrorMapType = {
        SuppressedError: RaiseError,
    }

    @error_map_decorator(error_map, RaiseError)
    def fn() -> None:
        raise SuppressedError

    with pytest.raises(RaiseError):
        fn()


def test_error_map_decorator_multiply_errors():
    error_map: ErrorMapType = {
        Suppressed1Error: Raise1Error,
        Suppressed2Error: Raise2Error,
        Suppressed3Error: Raise3Error,
    }

    @error_map_decorator(error_map, DefaultError)
    def fn1() -> None:
        raise Suppressed1Error

    @error_map_decorator(error_map, DefaultError)
    def fn2() -> None:
        raise Suppressed2Error

    @error_map_decorator(error_map, DefaultError)
    def fn3() -> None:
        raise Suppressed3Error

    with pytest.raises(Raise1Error):
        fn1()

    with pytest.raises(Raise2Error):
        fn2()

    with pytest.raises(Raise3Error):
        fn3()
