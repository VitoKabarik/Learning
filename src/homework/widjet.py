from string import digits

from homework import masks


def mask_account_card(type_and_num: str) -> str:
    """Обрабатывает строку с номером счёта/карты, маскируя его"""
    if len(type_and_num) < 20:
        raise ValueError('Укажите тип и корректный номер банковского счёта')
    bank_account_number = ''
    for i in range(len(type_and_num)):
        if type_and_num[i] in '0123456789':
            bank_account_number += type_and_num[i]
        elif bank_account_number != '' and type_and_num[i] not in ' -.':
            raise ValueError('Укажите номер счёта или карты слитно, через пробел, точку или дефис')
    if type_and_num[:4] == 'Счет' or type_and_num[:4] == 'Счёт':
        if len(bank_account_number) != 20:
            raise ValueError('Номер личного счёта должен состоять из 20 цифр')
        return type_and_num[:5] + masks.get_mask_account(bank_account_number)
    else:
        if len(bank_account_number) != 16:
            raise ValueError('Номер карты должен состоять из 16 цифр')
        x = type_and_num.index(bank_account_number[0])
        if len(type_and_num[:x]) < 4:
            raise ValueError('Укажите платёжную систему вашей карты')
        return type_and_num[:x] + masks.get_mask_card_number(bank_account_number)


def get_date(row_date: str) -> str:
    """Расшифровывает дату"""
    return row_date[8:10] + "." + row_date[5:7] + "." + row_date[:4]


'''
Частные случаи:
 - Счет 01234567890123456789
 - Счёт 01234.56789.01234.56789
 - Счёт 012-345-678-901-234-56789
 - 
 - Master Card 0123456789012345
 - Мир 0123 4567 8901 2345
 - Visa 0123-4567-8901-2345
'''
