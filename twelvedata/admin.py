from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import CurrencyModel

@admin.register(CurrencyModel)
class CurrencyModelAdmin(SingletonModelAdmin):
    pass