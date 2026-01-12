from sys import exc_info

import pytest

from homework.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import list_for_tests


def test_filter_by_currency(list_for_tests):
    gen_filter_by_currency = filter_by_currency(list_for_tests, 'USD')
    assert next(gen_filter_by_currency) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(gen_filter_by_currency) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert next(gen_filter_by_currency) == {
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
        }
    gen_filter_by_currency = filter_by_currency(list_for_tests, 'rub')
    assert next(gen_filter_by_currency) == {
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
        }
    assert next(gen_filter_by_currency) == {
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
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    with pytest.raises(StopIteration) as exc_gen_info:
        next(gen_filter_by_currency)
    assert str(exc_gen_info.value) == "Других транзакций с данной валютой нет в списке"
    gen_filter_by_currency = filter_by_currency(list_for_tests, '')
    with pytest.raises(StopIteration) as exc_gen_info:
        next(gen_filter_by_currency)
    assert str(exc_gen_info.value) == "Транзакций с данной валютой нет в списке"
    gen_filter_by_currency = filter_by_currency([], 'eur')
    with pytest.raises(StopIteration) as exc_gen_info:
        next(gen_filter_by_currency)
    assert str(exc_gen_info.value) == "Транзакций с данной валютой нет в списке"


def test_transaction_descriptions(list_for_tests):
    gen_transaction_descriptions = transaction_descriptions(list_for_tests)
    assert next(gen_transaction_descriptions) == "Перевод организации"
    assert next(gen_transaction_descriptions) == "Перевод со счета на счет"
    assert next(gen_transaction_descriptions) == "Перевод со счета на счет"
    assert next(gen_transaction_descriptions) == "Перевод с карты на карту"
    assert next(gen_transaction_descriptions) == "Перевод организации"
    with pytest.raises(StopIteration) as exc_gen_info:
        next(gen_transaction_descriptions)
    assert str(exc_gen_info.value) == "В списке больше нет транзакций"
    gen_transaction_descriptions = transaction_descriptions([])
    with pytest.raises(ValueError) as exc_gen_info:
        next(gen_transaction_descriptions)
    assert str(exc_gen_info.value) == "В списке нет ни одной транзакции"
    gen_transaction_descriptions = transaction_descriptions([
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
        }
    ])
    assert next(gen_transaction_descriptions) == "Перевод со счета на счет"
    assert next(gen_transaction_descriptions) == "Тип данной транзакции неизвестен"
    assert next(gen_transaction_descriptions) == "Перевод с карты на карту"

@pytest.mark.parametrize('first_num, last_num, expected_list',
                            [
                                (6, 1, [
                                        '0000 0000 0000 0001', '0000 0000 0000 0002',
                                        '0000 0000 0000 0003', '0000 0000 0000 0004',
                                        '0000 0000 0000 0005', '0000 0000 0000 0006']
                                ),
                                (1234567890123445, 1234567890123457, [
                                        '1234 5678 9012 3445', '1234 5678 9012 3446',
                                        '1234 5678 9012 3447', '1234 5678 9012 3448',
                                        '1234 5678 9012 3449', '1234 5678 9012 3450',
                                        '1234 5678 9012 3451', '1234 5678 9012 3452',
                                        '1234 5678 9012 3453', '1234 5678 9012 3454',
                                        '1234 5678 9012 3455', '1234 5678 9012 3456',
                                        '1234 5678 9012 3457']
                                ),
                                (594967, 594967, ['0000 0000 0059 4967']
                                )
                            ]
                         )
def test_card_number_generator(first_num, last_num, expected_list):
    gen_card_number_generator = card_number_generator(first_num, last_num)
    if last_num < first_num:
        quan_of_steps = first_num - last_num + 1
    else:
        quan_of_steps = last_num - first_num + 1
    for steps in range(quan_of_steps):
        assert next(gen_card_number_generator) == expected_list[steps]
    gen_card_number_generator = card_number_generator(8877776666, 8877776666)
    assert next(gen_card_number_generator) == '0000 0088 7777 6666'
    with pytest.raises(StopIteration) as exc_gen_info:
        next(gen_card_number_generator)
    assert str(exc_gen_info.value) == "Все возможные номера карт в предложенном интервале уже сгенерированы"

