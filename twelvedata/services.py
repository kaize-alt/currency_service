import os
import json

import requests

from rest_framework.response import Response

from .models import CurrencyModel


class TwelveDataService:
    API_KEY_TWELVE_DATA = os.getenv('API_KEY_TWELVE_DATA')
    BASE_URL_TWELVE_DATA = os.getenv('BASE_URL_TWELVE_DATA')

    def __init__(self, currency, comparison_currency):
        self.currency = currency
        self.comparison_currency = comparison_currency

    def get_exchange_rate(self):
        url = f"{self.BASE_URL_TWELVE_DATA}/exchange_rate"
        params = {
            "symbol": f"{self.currency}/{self.comparison_currency}",
            "apikey": self.API_KEY_TWELVE_DATA
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch exchange rate"}, status=500)

        data = response.json()

        if "rate" not in data:
            return Response({"error": "Invalid response from API"}, status=400)

        rate = data["rate"]
        currency_model = CurrencyModel.get_solo()
        currency_model.exchange_rate = rate
        currency_model.save()

        return Response({"rate": rate}, status=200)

"""class ApplicationService:
    BASE_URL_SAT = os.getenv('BASE_URL_SAT')

    def __init__(self, service_id):
        self.service_id = service_id

    def create_application(self):
        endpoint = f"{self.BASE_URL_SAT}/applications/?service_id={self.service_id}"

        request_body = {
            "name": "string",
            "surname": "string",
            "phone_number": "string",
            "email": "user@example.com",
            "address": "string",
            "selected_service_option": 0
        }
        headers = {
            "accept": "application / json",
            "Content-Type": "application/json",
            "X-CSRFToken": "0TOK3AA3n34NMfwpJPiYXD40Jg0Qc8RI1VH0KxmZRtYQMa8DtvmIpjXNrdxMjLCY",
        }
        response = requests.post(endpoint, headers=headers, json=request_body)
        response_json = response.json()

        return response_json"""
