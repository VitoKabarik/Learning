from typing import Any
from homework.masks import get_mask_account, get_mask_card_number


types_of_payments = [
    'СЧЕТ ', 'СЧЁТ ', 'MAESTRO ', 'MASTERCARD ', 'VISA CLASSIC ', 'VISA PLATINUM ', 'VISA GOLD ', 'МИР '
]


def mask_account_card(type_and_num: str) -> Any:
    """Обрабатывает строку с номером счёта/карты, маскируя его."""
    if len(type_and_num) < 20:
        raise ValueError("Некорректный банковский счёт")
    for i in range(len(type_and_num)):
        if type_and_num[i] in '0123456789':
            if type_and_num[:i].upper() not in types_of_payments:
                raise ValueError("Некорректная платёжная система")
            else:
                if type_and_num[:i].upper() in types_of_payments[:2]:
                    return type_and_num[:i] + get_mask_account(type_and_num[i:])
                else:
                    return type_and_num[:i] + get_mask_card_number(type_and_num[i:])
    raise ValueError("Отсутствует номер банковского счёта")


def check_date_on_correct(day: str, month: str, year: str) -> bool:
    """Проверяет получаемую дату на корректность."""
    long_months = ('01', '03', '05', '07', '08', '10', '12')
    if month == '02':
        if int(day) == 29:
            if int(year) % 4 == 0:
                return True
            else:
                return False
        elif int(day) in range(1, 29):
            return True
        else:
            return False
    elif int(day) not in range(1, 32):
        return False
    else:
        if int(day) == 31 and month not in long_months:
            return False
        else:
            return True


def get_date(row_date: str) -> str:
    """Расшифровывает дату."""
    if len(row_date) < 19:
        raise ValueError("Укажите дату и время проведения операции")
    if not row_date[:4].isdigit() or not row_date[5:7].isdigit() or not row_date[8:10].isdigit():
        raise TypeError("Дата должна состоять из цифр")
    if int(row_date[:4]) < 1980 or int(row_date[:4]) > 2025:
        raise ValueError("Укажите год проведения операции корректно")
    if int(row_date[5:7]) == 0 or int(row_date[5:7]) > 12:
        raise ValueError("Укажите месяц проведения операции корректно")
    if int(row_date[8:10]) == 0 or int(row_date[8:10]) > 31:
        raise ValueError("Укажите число проведения операции корректно")
    if check_date_on_correct(row_date[8:10], row_date[5:7], row_date[:4]):
        return f'{row_date[8:10]}.{row_date[5:7]}.{row_date[:4]}'
    else:
        raise ValueError("Укажите дату проведения операции в формате ГГГГ-ММ-ДД")
