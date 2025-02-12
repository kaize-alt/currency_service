from rest_framework import serializers
from .models import CurrencyModel


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = ("base_currency", "comparison_currency")


class ApplicationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=255)
    selected_service_option = serializers.IntegerField()
    service_id = serializers.IntegerField()
