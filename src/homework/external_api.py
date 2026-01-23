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
    from_cur = transaction.get('operationAmount').get('currency').get('code')
    amount = transaction.get('operationAmount').get('amount')
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

print(return_of_amount({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))
