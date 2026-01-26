import json
from typing import Any
import logging
import os


def show_transactions(path_to_json: str) -> Any:
    """Преобразует json-файл в строку Python."""
    try:
        with open(path_to_json, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError, FileNotFoundError):
        return []


path_to_utils_log = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'utils.log')
utils_logger = logging.getLogger(__name__)
utils_logger.propagate = False
f_handler_for_utils = logging.FileHandler(path_to_utils_log, mode='w', encoding='utf-8')
utils_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
f_handler_for_utils.setFormatter(utils_formatter)
utils_logger.addHandler(f_handler_for_utils)
utils_logger.setLevel(logging.DEBUG)