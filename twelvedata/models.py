from enum import Enum
from django.db import models
from solo.models import SingletonModel


class CurrencyEnum(str, Enum):
    USD = "USD"
    RUB = "RUB"


class CurrencyModel(SingletonModel):
    base_currency = models.CharField(
        max_length=3,
        choices=[(currency.value, currency.name) for currency in CurrencyEnum],
        default=CurrencyEnum.USD.value
    )
    comparison_currency = models.CharField(
        max_length=3,
        choices=[(currency.value, currency.name) for currency in CurrencyEnum],
        default=CurrencyEnum.RUB.value
    )
    exchange_rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=1.0000
    )

    def __str__(self):
        return f"{self.base_currency} to {self.comparison_currency}"
