import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from homework.utils import show_transactions

tst_data = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}
json_str = json.dumps(tst_data)


@patch("builtins.open", new_callable=mock_open, read_data=json_str)
def test_show_transactions(mock_file: MagicMock) -> None:
    """Тестирует функцию, преобразующую json-строку в строку Python."""
    assert show_transactions("some_path.json") == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_file.assert_called_once_with("some_path.json", encoding="utf-8")


@patch("json.load")
@patch("builtins.open")
@pytest.mark.parametrize(
    "exp_err, exp_output", [(FileNotFoundError(), []), (ValueError(), []), (json.JSONDecodeError("msg", "doc", 0), [])]
)
def test_show_transactions_with_wrong(
    mock_open_obj: MagicMock, mock_json: MagicMock, exp_err: Exception, exp_output: list
) -> None:
    """Тестирует функцию, преобразующую json-строку в строку Python.

    Проверяет её на корректный вывод при ошибках чтения или декодирования файла.
    """
    if isinstance(exp_err, json.JSONDecodeError):
        mock_json.side_effect = exp_err
    else:
        mock_open_obj.side_effect = exp_err
    assert show_transactions("some_path") == exp_output
    if isinstance(exp_err, json.JSONDecodeError):
        mock_json.assert_called_once()
    mock_open_obj.assert_called_once_with("some_path", encoding="utf-8")
