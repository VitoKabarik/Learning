import json
from typing import Any


def show_transactions(path_to_json: str) -> Any:
    """Преобразует json-файл в строку Python."""
    try:
        with open(path_to_json, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError, FileNotFoundError):
        return []
