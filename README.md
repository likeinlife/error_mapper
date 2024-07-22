# Error-mapper

[![image](https://img.shields.io/pypi/v/error-mapper.svg)](https://pypi.python.org/pypi/error-mapper)
[![image](https://img.shields.io/pypi/l/error-mapper.svg)](https://github.com/likeinlife/error_mapper/blob/main/LICENSE)
<a href="http://mypy-lang.org/" target="_blank"><img src="https://img.shields.io/badge/mypy-checked-1F5082.svg" alt="Mypy checked"></a>
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/pyversions/error-mapper.svg)](https://pypi.python.org/pypi/error-mapper)

Python error mapper based on decorators.

# Installing

`pip install error-mapper`

# Example

## Error map

```python
from error_mapper import ErrorMapType, error_map_decorator

class SuppressedError(Exception): ...

class RaiseError(Exception): ...

error_map: ErrorMapType = {
    SuppressedError: RaiseError,
}

@error_map_decorator(error_map, RaiseError)
def fn() -> None:
    raise SuppressedError
```

## On error execute

```python
from error_mapper import ErrorMapTypeExecute, on_error_execute

class SuppressedError(Exception): ...

class RaiseError(Exception): ...

def process_error(error: Exception) -> tp.NoReturn:
    raise RaiseError from error

error_map: ErrorMapTypeExecute = {
    SuppressedError: process_error,
}

@on_error_execute(error_map, RaiseError)
def fn() -> None:
    raise SuppressedError
```

## Suppress error to None

```python
from error_mapper import suppress_to_none


class SuppressedError(Exception): ...


class RaiseError(Exception): ...


@suppress_to_none(SuppressedError)
def fn() -> None:
    raise SuppressedError


assert fn() is None

```

# Testing, linting, formatting

- `rye test`
- `rye lint`
- `rye fmt`