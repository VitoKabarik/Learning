from typing import Any
from unittest.mock import MagicMock, patch
import pytest
from homework.external_api import return_of_amount


@patch("requests.request")
def test_return_of_amount_for_simple_output(mock_request: MagicMock, list_for_tests: list) -> None:
    """Тестирует функцию, возвращающую сумму транзакции в рублях."""
    assert return_of_amount(list_for_tests[2]) == 43318.34
    mock_request.assert_not_called()


@pytest.mark.parametrize(
    "invalid_transaction, exp_err",
    [
        (
            {
                "id": 522357576,
                "state": "EXECUTED",
                "date": "2019-07-12T20:41:47.882230",
                "operationAmount": {"amount": "51463.70"},
                "description": "Перевод организации",
                "from": "Счет 48894435694657014368",
                "to": "Счет 38976430693692818358",
            },
            "Валюта транзакции неизвестна",
        ),
        (
            {
                "id": 596171168,
                "state": "EXECUTED",
                "date": "2018-07-11T02:26:18.671407",
                "description": "Открытие вклада",
                "to": "Счет 72082042523231456215",
            },
            "Сумма транзакции неизвестна",
        ),
        (
            {
                "id": 172864002,
                "state": "EXECUTED",
                "date": "2018-12-28T23:10:35.459698",
                "operationAmount": {"amount": "Безд-возд-мезд-но!", "currency": {"name": "USD", "code": "USD"}},
                "description": "Открытие вклада",
                "to": "Счет 96231448929365202391",
            },
            "Некорректная сумма транзакции",
        ),
    ],
)
def test_return_of_amount_without_keys(invalid_transaction: dict, exp_err: str) -> None:
    """Тестирует функцию, возвращающую сумму транзакции в рублях, на некорректные вводные данные."""
    with pytest.raises((AttributeError, ValueError)) as exc_keyless_info:
        return_of_amount(invalid_transaction)
    assert str(exc_keyless_info.value) == exp_err


@patch("requests.request")
@pytest.mark.parametrize("stat_code, server_answer", [(200, {"result": 76.0}), (500, "Server Error")])
def test_return_of_amount_with_try_connecting(mock_request: MagicMock, stat_code: int, server_answer: Any) -> None:
    """Тестирует функцию, возвращающую сумму транзакции в рублях.

    Проверяет, что функция обращается к серверу и корректно обрабатывает полученные от него данные.
    """
    data_for_tst = {"operationAmount": {"amount": "1.0", "currency": {"name": "USD", "code": "USD"}}}
    mock_request.return_value.status_code = stat_code
    if stat_code == 200:
        mock_request.return_value.json.return_value = server_answer
        assert return_of_amount(data_for_tst) == 76.0
        mock_request.assert_called_once()
    else:
        mock_request.return_value.reason = server_answer
        with pytest.raises(Exception) as err:
            return_of_amount(data_for_tst)
        assert str(err.value) == server_answer
        mock_request.assert_called_once()
