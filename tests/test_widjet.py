import pytest

from src.homework.widjet import get_date, mask_account_card


@pytest.mark.parametrize(
    "bank_datas, expected_result_account",
    [
        ("Счёт 01234567890123456789", "Счёт **6789"),
        ("Счет 01234 56789 01234 56789", "Счет **6789"),
        ("Счёт 012.345.678.901.234.56789", "Счёт **6789"),
        ("Счет 0123-4567-8901-2345-6789", "Счет **6789"),
        ("Visa 0123456789012345", "Visa 0123 45** **** 2345"),
        ("Mastercard 0000    1111  2222      3333", "Mastercard 0000 11** **** 3333"),
        ("Мир 0123.45678901 2345", "Мир 0123 45** **** 2345"),
    ],
)
def test_mask_account_card(bank_datas: str, expected_result_account: str) -> None:
    """Тестирует функцию, маскирующую номер счёта или карты, на определённых строках."""
    assert mask_account_card(bank_datas) == expected_result_account


def test_mask_account_card_with_empty_str() -> None:
    """Тестирует функцию, маскирующую номер счёта или карты, на работу со вводом пустой строки."""
    with pytest.raises(ValueError) as exc_info_empty:
        mask_account_card("")
    assert str(exc_info_empty.value) == "Укажите вид и корректный номер банковского счёта"


def test_mask_account_card_with_invalid_symbols() -> None:
    """Тестирует функцию, маскирующую номер счёта или карты, на работу со вводом некорректных символов."""
    with pytest.raises(ValueError) as exc_info_symbols:
        mask_account_card("Мир 0123?4567?8901?2345.")
    assert str(exc_info_symbols.value) == "Укажите номер счёта или карты слитно, через пробел, точку или дефис"


def test_mask_account_card_with_invalid_quantity_of_numbers() -> None:
    """Тестирует функцию, маскирующую номер счёта или карты, на неверную длину строки ввода."""
    with pytest.raises(ValueError) as exc_info_account:
        mask_account_card("Счёт 0123 4567 8901 2345")
    assert str(exc_info_account.value) == "Номер личного счёта должен состоять из 20 цифр"
    with pytest.raises(ValueError) as exc_info_card:
        mask_account_card("Mastercard 01234 56789 01234 567")
    assert str(exc_info_card.value) == "Номер карты должен состоять из 16 цифр"


def test_mask_account_card_with_invalid_payment_system() -> None:
    """Тестирует функцию, маскирующую номер счёта или карты.

    Проверяет работу функции с номером счёта при некорректном указании платёжной системы
    или его отсутствии.
    """
    with pytest.raises(ValueError) as exc_info_pay:
        mask_account_card("Hi 0123 4567 8901 2345")
    assert str(exc_info_pay.value) == "Укажите платёжную систему вашей карты"


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
