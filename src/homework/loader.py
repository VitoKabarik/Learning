from typing import Any

import pandas as pd


def read_data_from(path_to_file: str, file_type: str) -> Any:
    """Читает данные из csv- и excel-файлов."""
    try:
        if file_type == "csv":
            reviews = pd.read_csv(path_to_file, sep=None, engine="python", encoding="utf-8")
        else:
            reviews = pd.read_excel(path_to_file)
        return reviews.to_dict(orient="records")
    except (FileNotFoundError, pd.errors.ParserError, pd.errors.EmptyDataError, PermissionError):
        return []


def load_csv(path_to_csv: str) -> Any:
    """Принимает путь к csv-файлу и возвращает данные из него в виде списка."""
    return read_data_from(path_to_csv, "csv")


def load_excel(path_to_excel: str) -> Any:
    """Принимает путь к excel-файлу и возвращает данные из него в виде списка."""
    return read_data_from(path_to_excel, "excel")
