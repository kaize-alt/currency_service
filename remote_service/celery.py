import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remote_service.settings")

app = Celery("remote_service")

app.config_from_object('remote_service.settings', namespace="CELERY")

app.autodiscover_tasks()
