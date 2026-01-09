def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return result


def get_mask_account(account: str) -> str:
    """Маскирует номер лицевого счёта."""
    return "**" + account[-4:]
