import os

import requests
from celery import shared_task
from .services import TwelveDataService
from .models import CurrencyModel

BASE_URL_SAT = os.getenv('BASE_URL_SAT')
X_SRFTOKEN = os.getenv('X_SRFTOKEN')

@shared_task
def update_exchange_rate():
    base_currency = 'USD'
    comparison_currency = 'RUB'

    service = TwelveDataService(base_currency, comparison_currency)

    response = service.get_exchange_rate()

    if response.status_code == 200:
        rate = response.data.get('rate')
        currency_model = CurrencyModel.get_solo()
        currency_model.exchange_rate = rate
        currency_model.save()

    return response.data


@shared_task
def create_application(data):
    endpoint = f"{BASE_URL_SAT}/applications/?service_id={data['service_id']}"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": X_SRFTOKEN,
    }

    response = requests.post(endpoint, headers=headers, json=data)

    return response.json()
