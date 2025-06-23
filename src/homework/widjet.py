from homework import masks


def mask_account_card(type_and_num: str) -> str:
    """Обрабатывает строку с номером счёта/карты, маскируя его"""
    if type_and_num[:4] == "Счет":
        return type_and_num[:5] + masks.get_mask_account(type_and_num)
    else:
        return type_and_num[:-16] + masks.get_mask_card_number(type_and_num[-16:])


def get_date(row_date: str) -> str:
    """Расшифровывает дату"""
    return row_date[8:10] + "." + row_date[5:7] + "." + row_date[:4]
