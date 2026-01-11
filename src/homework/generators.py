

def filter_by_currency(list_of_transactions: list, currency: str):
    suitable_transactions = []
    currency = currency.upper()
    for i in range(len(list_of_transactions)):
        for details_of_transactions in list_of_transactions[i].keys():
            if type(list_of_transactions[i][details_of_transactions]) == dict:
                temp_cell = list_of_transactions[i][details_of_transactions]
                if 'currency' in temp_cell:
                    if type(temp_cell['currency']) == dict:
                        suitable = True
                        for check_for_currency in temp_cell['currency'].values():
                            if check_for_currency != currency:
                                suitable = False
                                break
                        if suitable:
                            suitable_transactions.append(list_of_transactions[i])
                            yield list_of_transactions[i]



def transaction_descriptions():
    yield


def card_number_generator(start: int, stop: int):
    if stop < start:
        i = start
        start = stop
        stop = i
    while start <= stop:
        card_number = '0' * (16 - len(str(start))) + str(start)
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}'
        start += 1

test_list = [
{
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
      },
      {
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
       },
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "RUB",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
]