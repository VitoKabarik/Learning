from string import digits

from homework import masks


def mask_account_card(type_and_num: str) -> str:
    """Обрабатывает строку с номером счёта/карты, маскируя его"""
    if len(type_and_num) < 20:
        raise ValueError("Укажите тип и корректный номер банковского счёта")
    bank_account_number = ""
    for i in range(len(type_and_num)):
        if type_and_num[i] in "0123456789":
            bank_account_number += type_and_num[i]
        elif bank_account_number != "" and type_and_num[i] not in " -.":
            raise ValueError("Укажите номер счёта или карты слитно, через пробел, точку или дефис")
    if type_and_num[:4] == "Счет" or type_and_num[:4] == "Счёт":
        if len(bank_account_number) != 20:
            raise ValueError("Номер личного счёта должен состоять из 20 цифр")
        return type_and_num[:5] + masks.get_mask_account(bank_account_number)
    else:
        if len(bank_account_number) != 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")
        x = type_and_num.index(bank_account_number[0])
        if len(type_and_num[:x]) < 4:
            raise ValueError("Укажите платёжную систему вашей карты")
        return type_and_num[:x] + masks.get_mask_card_number(bank_account_number)


def check_date_on_correct(day: str, month: str, year: str) -> bool:
    long_months = ("01", "03", "05", "07", "08", "10", "12")
    if month == "02":
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
    """Расшифровывает дату"""
    if len(row_date) < 19:
        raise ValueError("Укажите дату и время проведения операции")
    if row_date[:4].isdigit() == False or row_date[5:7].isdigit() == False or row_date[8:10].isdigit() == False:
        raise TypeError("Дата должна состоять из цифр")
    if int(row_date[:4]) < 1980 or int(row_date[:4]) > 2025:
        raise ValueError("Укажите год проведения операции корректно")
    if int(row_date[5:7]) == 0 or int(row_date[5:7]) > 12:
        raise ValueError("Укажите месяц проведения операции корректно")
    if int(row_date[8:10]) == 0 or int(row_date[8:10]) > 31:
        raise ValueError("Укажите число проведения операции корректно")
    if check_date_on_correct(row_date[8:10], row_date[5:7], row_date[:4]):
        return f"{row_date[8:10]}.{row_date[5:7]}.{row_date[:4]}"
    else:
        raise ValueError("Укажите дату проведения операции в формате ГГГГ-ММ-ДД")