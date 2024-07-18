# Description

Decorator error mapper

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

# Testing, linting, formatting

- `rye test`
- `rye lint`
- `rye fmt`