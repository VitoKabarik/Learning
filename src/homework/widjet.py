import masks

def mask_account_card(type_and_num: str) -> str:
    if type_and_num[:4] == "Счет":
        return type_and_num[:5] + masks.get_mask_account(type_and_num)
    else:
        return type_and_num[:-16] + masks.get_mask_card_number(type_and_num[-16:])


def get_date():
    pass

print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Счет 64686473678894779589'))
print(mask_account_card('MasterCard 7158300734726758'))
print(mask_account_card('Счет 35383033474447895560'))
print(mask_account_card('Visa Classic 6831982476737658'))
print(mask_account_card('Visa Platinum 8990922113665229'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 73654108430135874305'))