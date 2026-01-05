from src.homework.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тестирует функцию, маскирующую номер карты."""
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("") == " ** **** "
    assert get_mask_card_number("q") == "q ** **** q"


def test_get_mask_account() -> None:
    """Тестирует функцию, маскирующую номер лицевого счёта."""
    assert get_mask_account("01234567891011121314") == "**1314"
    assert get_mask_account("") == "**"
    assert get_mask_account("*") == "***"
