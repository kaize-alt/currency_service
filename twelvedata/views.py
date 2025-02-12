from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import mixins
from .serializers import ExchangeRateSerializer, ApplicationSerializer
from .services import TwelveDataService
from .tasks import create_application

class ExchangeRateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ExchangeRateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        base_currency = serializer.validated_data["base_currency"]
        comparison_currency = serializer.validated_data["comparison_currency"]

        service = TwelveDataService(base_currency, comparison_currency)

        exchange_rate_response = service.get_exchange_rate()

        if exchange_rate_response.status_code != status.HTTP_200_OK:
            return Response(
                exchange_rate_response.data, status=exchange_rate_response.status_code
            )

        return Response(exchange_rate_response.data)


class ApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_application.delay(serializer.validated_data)

        return Response({"message": "Application is being processed"}, status=status.HTTP_202_ACCEPTED)
