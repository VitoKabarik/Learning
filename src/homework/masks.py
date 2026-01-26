import logging
import os


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return result


def get_mask_account(account: str) -> str:
    """Маскирует номер лицевого счёта."""
    return "**" + account[-4:]


path_to_masks_log = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'masks.log')
masks_logger = logging.getLogger(__name__)
masks_logger.propagate = False
f_handler_for_masks = logging.FileHandler(path_to_masks_log, mode='w', encoding='utf-8')
masks_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
f_handler_for_masks.setFormatter(masks_formatter)
masks_logger.addHandler(f_handler_for_masks)
masks_logger.setLevel(logging.DEBUG)