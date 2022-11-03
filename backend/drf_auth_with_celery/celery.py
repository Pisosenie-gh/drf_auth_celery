import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_auth_with_celery.settings')

app = Celery('send_email')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
