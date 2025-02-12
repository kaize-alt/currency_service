from rest_framework import routers

from .views import ExchangeRateViewSet, ApplicationViewSet


twelvedata_router = routers.DefaultRouter()

twelvedata_router.register(r"exchange-rate", ExchangeRateViewSet, basename="exchange_rate")
twelvedata_router.register(r"create-applications", ApplicationViewSet, basename="create_application")
