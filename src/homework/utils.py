import json
from typing import Any

from homework.logger import setup_logging

utils_logger = setup_logging("utils", "utils.log")


def show_transactions(path_to_json: str) -> Any:
    """Преобразует json-файл в строку Python."""
    try:
        with open(path_to_json, encoding="utf-8") as f:
            utils_logger.info("Успешное преобразование json-файла")
            return json.load(f)
    except (json.JSONDecodeError, ValueError, FileNotFoundError):
        utils_logger.error("Неудачная попытка преобразования json-файла")
        return []
