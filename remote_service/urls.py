from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from rest_framework import routers

from twelvedata.urls import twelvedata_router


router = routers.DefaultRouter()
router.registry.extend(twelvedata_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
