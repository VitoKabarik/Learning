import pytest
from typing import Any
from src.homework.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("potential_card_number, exp_output", [
    ('9999222288881111', '9999 22** **** 1111'),
    ('0123?4567!8901 Тут можно написать что угодно 2345', '0123 45** **** 2345'),
    ('0123 4567 8901', ValueError()),
    ('1111 2222 3333 4444 5555 6666 7777 8888 9999 0000', ValueError())
])
def test_get_mask_card_number(potential_card_number: str, exp_output: Any) -> None:
    """Тестирует функцию, маскирующую номер карты."""
    if isinstance(exp_output, Exception):
        with pytest.raises(ValueError) as err_info:
            get_mask_card_number(potential_card_number)
        assert str(err_info.value) == "Некорректный номер карты"
    else:
        assert get_mask_card_number(potential_card_number) == exp_output


@pytest.mark.parametrize("potential_account, exp_output", [
    ('00005555777733339999', '**9999'),
    ('01-23-45-67-89 И здесь тоже 01+23+45+67+89', '**6789'),
    ('1111 2222 3333 4444', ValueError()),
    ('0987654321 0987654321 0987654321', ValueError())
])
def test_get_mask_account(potential_account: str, exp_output: Any) -> None:
    """Тестирует функцию, маскирующую номер лицевого счёта."""
    if isinstance(exp_output, Exception):
        with pytest.raises(ValueError) as err_info:
            get_mask_account(potential_account)
        assert str(err_info.value) == "Некорректный номер лицевого счёта"
    else:
        assert get_mask_account(potential_account) == exp_output
