import requests

from rest_framework.response import Response

from .models import CurrencyModel

class TwelveDataService:
    API_KEY = 'ce01ff241cc64fd983b3bc4673de2ae4'
    BASE_URL = 'https://api.twelvedata.com'

    def __init__(self, currency, comparison_currency):
        self.currency = currency
        self.comparison_currency = comparison_currency

    def get_exchange_rate(self):
        url = f"{self.BASE_URL}/exchange_rate"
        params = {
            "symbol": f"{self.currency}/{self.comparison_currency}",
            "apikey": self.API_KEY
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
