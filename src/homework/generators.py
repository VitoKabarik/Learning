

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
                yield "Отсутствует описание транзакции"
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

transactions = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
]
