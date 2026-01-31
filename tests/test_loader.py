from typing import Union
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from homework.loader import load_csv, load_excel


@patch("pandas.read_csv")
@pytest.mark.parametrize(
    "csv_data, exp_output",
    [
        (pd.DataFrame([{"То": "Одно"}, {"То": "Другое"}]), [{"То": "Одно"}, {"То": "Другое"}]),
        (pd.DataFrame(), []),
        (FileNotFoundError, []),
    ],
)
def test_load_csv(mock_read: MagicMock, csv_data: Union, exp_output: list) -> None:
    """Тестирует функцию, считывающую данные из csv-файла."""
    if isinstance(csv_data, type) and issubclass(csv_data, Exception):
        mock_read.side_effect = csv_data
    else:
        mock_read.return_value = csv_data
    assert load_csv("some_path.csv") == exp_output
    mock_read.assert_called_once_with("some_path.csv", sep=None, engine="python", encoding="utf-8")


@patch("pandas.read_excel")
@pytest.mark.parametrize(
    "excel_data, exp_output",
    [
        (pd.DataFrame([{"То": "Одно"}, {"То": "Другое"}]), [{"То": "Одно"}, {"То": "Другое"}]),
        (pd.DataFrame(), []),
        (FileNotFoundError, []),
    ],
)
def test_load_excel(mock_read: MagicMock, excel_data: Union, exp_output: list) -> None:
    """Тестирует функцию, считывающую данные из excel-файла."""
    if isinstance(excel_data, type) and issubclass(excel_data, Exception):
        mock_read.side_effect = excel_data
    else:
        mock_read.return_value = excel_data
    assert load_excel("some_path.xlsx") == exp_output
    mock_read.assert_called_once_with("some_path.xlsx")
