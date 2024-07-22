import typing as tp

import pytest
from error_mapper import ErrorMapTypeExecute, on_error_execute

from tests.mocks import (
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


def test_on_error_execute():
    check_flag = False

    def process_error(error: Exception) -> tp.NoReturn:
        nonlocal check_flag
        check_flag = True
        raise RaiseError from error

    error_map: ErrorMapTypeExecute = {
        SuppressedError: process_error,
    }

    @on_error_execute(error_map, DefaultError)
    def fn() -> None:
        raise SuppressedError

    with pytest.raises(RaiseError):
        fn()

    assert check_flag


def test_on_error_execute_unexpected():
    error_map: ErrorMapTypeExecute = {}

    @on_error_execute(error_map, DefaultError)
    def fn() -> None:
        raise ValueError

    with pytest.raises(DefaultError):
        fn()


def test_on_error_execute_multiply():
    checkbox1, checkbox2, checkbox3 = False, False, False

    def process_error(error: Exception) -> tp.NoReturn:
        nonlocal checkbox1, checkbox2, checkbox3
        match error:
            case Suppressed1Error():
                checkbox1 = True
                raise Raise1Error
            case Suppressed2Error():
                checkbox2 = True
                raise Raise2Error
            case Suppressed3Error():
                checkbox3 = True
                raise Raise3Error
            case _:
                raise error

    error_map: ErrorMapTypeExecute = {
        Suppressed1Error: process_error,
        Suppressed2Error: process_error,
        Suppressed3Error: process_error,
    }

    @on_error_execute(error_map, DefaultError)
    def fn1() -> None:
        raise Suppressed1Error

    @on_error_execute(error_map, DefaultError)
    def fn2() -> None:
        raise Suppressed2Error

    @on_error_execute(error_map, DefaultError)
    def fn3() -> None:
        raise Suppressed3Error

    with pytest.raises(Raise1Error):
        fn1()
    assert checkbox1

    with pytest.raises(Raise2Error):
        fn2()
    assert checkbox2

    with pytest.raises(Raise3Error):
        fn3()
    assert checkbox2
