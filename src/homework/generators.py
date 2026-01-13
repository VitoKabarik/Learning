from collections.abc import Iterator


def filter_by_currency(list_of_transactions: list, currency: str) -> Iterator:
    """Выдаёт по запросу транзакции с указанной валютой."""
    suitable_transactions = []
    for i in range(len(list_of_transactions)):
        if list_of_transactions[i].get('operationAmount').get('currency').get('code') == currency.upper():
            suitable_transactions.append(list_of_transactions[i])
            yield list_of_transactions[i]
    if not suitable_transactions:
        raise RuntimeError("Транзакций с данной валютой нет в списке")
    else:
        raise RuntimeError("Других транзакций с данной валютой нет в списке")


def transaction_descriptions(list_of_transactions: list) -> Iterator:
    """Описывает по запросу тип транзакций в предложенном списке."""
    if not list_of_transactions:
        raise ValueError("В списке нет ни одной транзакции")
    else:
        for i in range(len(list_of_transactions)):
            if 'description' in list_of_transactions[i]:
                yield list_of_transactions[i]['description']
            else:
                yield "Тип данной транзакции неизвестен"
        raise RuntimeError("В списке больше нет транзакций")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генерирует номера карт в указанном интервале."""
    if stop < start:
        o = start
        start = stop
        stop = o
    while start <= stop:
        card_number = '0' * (16 - len(str(start))) + str(start)
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}'
        start += 1
    raise RuntimeError("Все возможные номера карт в указанном интервале уже сгенерированы")
