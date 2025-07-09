from homework.widjet import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card('Счет 01234567891011121314') == 'Счет **1314'
    assert mask_account_card('Maestro 1234567890123456') == 'Maestro 1234 56** **** 3456'
    assert mask_account_card('') == ' ** **** '
    assert mask_account_card('В случае зомби-апокалипсиса звонить по номеру: -273(666)%&$#789') == 'В случае зомби-апокалипсиса звонить по номеру: -273 (6** **** #789'


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
    assert get_date('') == '..'
    assert get_date('Дата') == '..Дата'
    assert get_date('Тест не проходит, но и не падает') == 'пр.не.Тест'
