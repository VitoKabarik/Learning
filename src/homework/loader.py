import pandas as pd
from typing import Any


def read_data_from(path_to_file: str, file_type: str) -> Any:
    try:
        if file_type == 'csv':
            reviews = pd.read_csv(path_to_file, sep=None, engine='python', encoding='utf-8')
        else:
            reviews = pd.read_excel(path_to_file)
        return reviews.to_dict(orient='records')
    except Exception:
        raise Exception("Не удалось прочитать данные: файл не существует или повреждён")


def load_csv(path_to_csv: str):
    return read_data_from(path_to_csv, 'csv')


def load_excel(path_to_excel: str) -> list:
    return read_data_from(path_to_excel, 'excel')
