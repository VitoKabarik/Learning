import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str="") -> Callable:
    """Декоратор, отслеживающий работу функции."""

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: tuple[Any], **kwargs: Any) -> Any:
            mess_from_log = ""
            err = None
            try:
                result = function(*args, **kwargs)
                mess_from_log = f"{time.ctime()} {function.__name__} ok"
                return result
            except Exception as e:
                err = e
                mess_from_log = f"{time.ctime()} {function.__name__} {type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{mess_from_log}\n")
                else:
                    print(mess_from_log)
                if err:
                    raise err

        return wrapper

    return decorator
