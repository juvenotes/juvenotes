import os
import sys

from django.apps import apps

from celery import Celery
from decouple import config

from .celerybeat_schedule import CELERYBEAT_SCHEDULE


settings_module = 'juvenotes.settings.production' if os.getenv('DJANGO_SETTINGS_MODULE') == 'juvenotes.settings.production' else config("DJANGO_SETTINGS_MODULE")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
if settings_module is None:
    print(
        "Error: no DJANGO_SETTINGS_MODULE found. Will NOT start devserver. "
        "Remember to create .env file at project root. "
        "Check README for more info."
    )
    sys.exit(1)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

app = Celery("juvenotes_tasks")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
app.conf.update(CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE)