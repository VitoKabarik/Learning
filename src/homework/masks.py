def get_mask_card_number(card_number: str) -> str:
    """Функция, которая делает маску номера карты."""
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return result


def get_mask_account(account: str) -> str:
    """Функция, которая делает маску личного счёта"""
    return "**" + account[-4:]
