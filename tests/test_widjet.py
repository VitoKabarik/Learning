import pytest
from src.homework.widjet import get_date, mask_account_card


@pytest.mark.parametrize("bank_datas, exp_output", [
    ('Счет 44238164562083919420', 'Счет **9420'),
    ('Visa Gold 7756673469642839', 'Visa Gold 7756 67** **** 2839'),
    ('Мир 1582   4744 75 54 7 3 0 1', 'Мир 1582 47** **** 7301'),
])
def test_mask_account_card(bank_datas: str, exp_output: str) -> None:
    """Тестирует функцию, возвращающую строку с замаскированными данными."""
    assert mask_account_card(bank_datas) == exp_output


@pytest.mark.parametrize("bank_datas, exp_err_msg", [
    ("", "Некорректный банковский счёт"),
    ('Visa Plotina 7756673469642839', "Некорректная платёжная система"),
    ('Мир без цифр: очередной бестселлер', "Отсутствует номер банковского счёта")
])
def test_mask_account_card_with_invalid_datas(bank_datas: str, exp_err_msg: str) -> None:
    """Тестирует функцию, возвращающую строку с замаскированными данными, на обработку некорректных данных."""
    with pytest.raises(ValueError) as data_err_info:
        mask_account_card(bank_datas)
    assert str(data_err_info.value) == exp_err_msg


@pytest.mark.parametrize(
    "date_of_operation, expected_result_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1992+02+29T19+39+57", "29.02.1992"),
        ("2003m11d10h10m50c30u123456", "10.11.2003"),
    ],
)
def test_get_date(date_of_operation: str, expected_result_date: str) -> None:
    """Тестирует функцию, проверяющую дату, на определённых строках."""
    assert get_date(date_of_operation) == expected_result_date


def test_get_date_with_empty_str() -> None:
    """Тестирует функцию, проверяющую дату, на работу с пустой строкой."""
    with pytest.raises(ValueError) as exc_info_empty:
        get_date("")
    assert str(exc_info_empty.value) == "Укажите дату и время проведения операции"


def test_get_date_with_invalid_symbols() -> None:
    """Тестирует функцию, проверяющую дату, на работу с некорректными символами."""
    with pytest.raises(TypeError) as exc_info_symbols:
        get_date("1b24-09-10T14:25:03")
    assert str(exc_info_symbols.value) == "Дата должна состоять из цифр"
