

def filter_by_currency(list_of_transactions: list, currency: str):
    suitable_transactions = []
    currency = currency.upper()
    for i in range(len(list_of_transactions)):
        for details_of_transactions in list_of_transactions[i].keys():
            if type(list_of_transactions[i][details_of_transactions]) == dict:
                temp_cell = list_of_transactions[i][details_of_transactions]
                if 'currency' in temp_cell:
                    if type(temp_cell['currency']) == dict and 'code' in temp_cell['currency']:
                        if temp_cell['currency']['code'] == currency:
                            suitable_transactions.append(list_of_transactions[i])
                            yield list_of_transactions[i]
    if not suitable_transactions:
        return "Транзакций с данной валютой нет в списке"
    else:
        return "Других транзакций с данной валютой нет в списке"


def transaction_descriptions(list_of_transactions: list):
    if not list_of_transactions:
        raise ValueError("В списке нет ни одной транзакции")
    else:
        for i in range(len(list_of_transactions)):
            if 'description' in list_of_transactions[i]:
                yield list_of_transactions[i]['description']
            else:
                yield "Тип данной транзакции неизвестен"
        return "В списке больше нет транзакций"


def card_number_generator(start: int, stop: int):
    if stop < start:
        o = start
        start = stop
        stop = o
    while start <= stop:
        card_number = '0' * (16 - len(str(start))) + str(start)
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}'
        start += 1
    return "Все возможные номера карт в предложенном интервале уже сгенерированы"
