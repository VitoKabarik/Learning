import os
import tempfile
import time
from typing import Any, Union

import pytest

from homework.decorators import log


def test_log(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирует декоратор, логирующий работу функции."""
    with tempfile.NamedTemporaryFile(mode="a+t", delete=False) as tf:
        logfile = tf.name

    @log(logfile)
    def division_with_round(a: int, b: int) -> float:
        """Функция для проверки. Делит одно число на другое."""
        return round(a / b, 2)

    division_with_round(17, 5)
    now = time.ctime()
    with open(logfile, "r") as tfl:
        result_str = tfl.read()
    assert result_str == f"{now} division_with_round ok\n"

    open(logfile, "w").close()
    now = time.ctime()
    with pytest.raises(ZeroDivisionError):
        division_with_round(3, 0)
    with open(logfile, "r") as lf:
        result_str = lf.read()
    assert result_str == f"{now} division_with_round ZeroDivisionError: division by zero. Inputs: (3, 0), {{}}\n"
    if os.path.exists(logfile):
        os.remove(logfile)

    @log()
    def search_key(dictionary: dict, the_key: Union[str | int]) -> Any:
        """Функция для проверки. Возвращает из словаря значение по указанному ключу."""
        return dictionary[the_key]

    some_dict = {"apple": "manzana", "water": "agua", "drink": "beber", "sun": "Sol"}

    assertion_value = search_key(some_dict, "water")
    now = time.ctime()
    captured = capsys.readouterr()
    assert captured.out == f"{now} search_key ok\n"
    assert assertion_value == "agua"

    with pytest.raises(KeyError):
        search_key(some_dict, "orange")
    now = time.ctime()
    captured = capsys.readouterr()
    assert captured.out == f"{now} search_key KeyError: 'orange'. Inputs: ({str(some_dict)}, 'orange'), {{}}\n"

    with pytest.raises(TypeError):
        search_key()
    now = time.ctime()
    captured = capsys.readouterr()
    assert f"{now} search_key TypeError:" in captured.out
    assert "test_log.<locals>.search_key() missing 2 required positional arguments:" in captured.out
    assert "'dictionary' and 'the_key'. Inputs: (), {}\n" in captured.out

    @log()
    def concatenation(str1: str, str2: str, str3: str, str4: str) -> str:
        """Функция для проверки. Соединяет указанные строки в одну."""
        return str1 + str2 + str3 + str4

    with pytest.raises(TypeError):
        concatenation(str1="Python ", str2="is very ", str3=True, str4="language")
    now = time.ctime()
    captured = capsys.readouterr()
    assertion_kwargs = "{'str1': 'Python ', 'str2': 'is very ', 'str3': True, 'str4': 'language'}"
    assert f"{now} concatenation TypeError:" in captured.out
    assert f'can only concatenate str (not "bool") to str. Inputs: (), {assertion_kwargs}\n' in captured.out
