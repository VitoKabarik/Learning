import logging
import os

from homework.logger import setup_logging


masks_logger = setup_logging('masks', 'masks.log')


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    result = ''
    for sym in card_number:
        if sym in '0123456789':
            result += sym
    if len(result) != 16:
        masks_logger.error("Неудачная попытка замаскировать номер карты")
        raise ValueError("Некорректный номер карты")
    masks_logger.info("Номер карты успешно замаскирован")
    return f"{result[:4]} {result[4:6]}** **** {result[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер лицевого счёта."""
    result = ''
    for sym in account:
        if sym in '0123456789':
            result += sym
    if len(result) != 20:
        masks_logger.error("Неудачная попытка замаскировать номер лицевого счёта")
        raise ValueError("Некорректный номер лицевого счёта")
    masks_logger.info("Номер лицевого счёта успешно замаскирован")
    return f"**{result[-4:]}"


print(get_mask_card_number('0000111122223333'))
print(get_mask_account('0000111122223333'))