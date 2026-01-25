import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('API_KEY')
headers= {
  'apikey': api_token
}


def return_of_amount(transaction: dict) -> float:
    from_cur = transaction.get('operationAmount', {}).get('currency', {}).get('code')
    amount = transaction.get('operationAmount', {}).get('amount')
    if not amount:
        raise AttributeError('Сумма транзакции неизвестна')
    if not from_cur:
        raise AttributeError('Валюта транзакции неизвестна')
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError('Некорректная сумма транзакции')
    if from_cur == 'USD' or from_cur == 'EUR':
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"amount": amount, "from": from_cur, "to": "RUB"}
        response = requests.request("GET", url, headers=headers, params=payload)
        status_code = response.status_code
        if status_code == 200:
            json_data = response.json()
            amount = round(json_data.get('result'), 2)
        else:
            raise Exception(response.reason)
    return amount
