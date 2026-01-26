import logging
import os


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    result = ''
    for sym in card_number:
        if sym in '0123456789':
            result += sym
    if len(result) != 16:
        raise ValueError("Некорректный номер карты")
    return f"{result[:4]} {result[4:6]}** **** {result[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер лицевого счёта."""
    result = ''
    for sym in account:
        if sym in '0123456789':
            result += sym
    if len(result) != 20:
        raise ValueError("Некорректный номер лицевого счёта")
    return f"**{result[-4:]}"


path_to_masks_log = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'logs', 'masks.log')
masks_logger = logging.getLogger(__name__)
masks_logger.propagate = False
f_handler_for_masks = logging.FileHandler(path_to_masks_log, mode='w', encoding='utf-8')
masks_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
f_handler_for_masks.setFormatter(masks_formatter)
masks_logger.addHandler(f_handler_for_masks)
masks_logger.setLevel(logging.DEBUG)
