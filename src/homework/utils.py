import json
import os


def show_transactions(path_to_json: str) -> list | dict:
    try:
        with open(path_to_json, encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError, FileNotFoundError):
        return []
