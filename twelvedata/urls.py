from rest_framework import routers

from .views import ExchangeRateViewSet


twelvedata_router = routers.DefaultRouter()

twelvedata_router.register(r"exchange-rate", ExchangeRateViewSet, basename="exchange_rate")
