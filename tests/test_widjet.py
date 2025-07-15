from sys import exc_info

from homework.widjet import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("bank_datas, expected_result", [
        ('Счёт 01234567890123456789', 'Счёт **6789'),
        ('Счет 01234 56789 01234 56789', 'Счет **6789'),
        ('Счёт 012.345.678.901.234.56789', 'Счёт **6789'),
        ('Счет 0123-4567-8901-2345-6789', 'Счет **6789'),
        ('Visa 0123456789012345', 'Visa 0123 45** **** 2345'),
        ('Mastercard 0000    1111  2222      3333', 'Mastercard 0000 11** **** 3333'),
        ('Мир 0123.45678901 2345', 'Мир 0123 45** **** 2345')
    ])

def test_mask_account_card(bank_datas, expected_result):
    assert mask_account_card(bank_datas) == expected_result
def test_mask_account_card_with_empty_str():
    with pytest.raises(ValueError) as exc_info_empty:
        mask_account_card('')
    assert str(exc_info_empty.value) == 'Укажите тип и корректный номер банковского счёта'
def test_mask_account_card_with_invalid_symbols():
    with pytest.raises(ValueError) as exc_info_symbols:
        mask_account_card('Мир 0123?4567?8901?2345.')
    assert str(exc_info_symbols.value) == 'Укажите номер счёта или карты слитно, через пробел, точку или дефис'
def test_mask_account_card_with_invalid_quantity_of_numbers():
    with pytest.raises(ValueError) as exc_info_account:
        mask_account_card('Счёт 0123 4567 8901 2345')
    assert str(exc_info_account.value) == 'Номер личного счёта должен состоять из 20 цифр'
    with pytest.raises(ValueError) as exc_info_card:
        mask_account_card('Mastercard 01234 56789 01234 567')
    assert str(exc_info_card.value) == 'Номер карты должен состоять из 16 цифр'
def test_mask_account_card_with_invalid_payment_system():
    with pytest.raises(ValueError) as exc_info_pay:
        mask_account_card('Hi 0123 4567 8901 2345')
    assert str(exc_info_pay.value) == 'Укажите платёжную систему вашей карты'


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
    assert get_date('') == '..'
    assert get_date('Дата') == '..Дата'
    assert get_date('Тест не проходит, но и не падает') == 'пр.не.Тест'
