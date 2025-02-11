from rest_framework import serializers
from .models import CurrencyModel


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = ("base_currency", "comparison_currency")
