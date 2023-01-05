import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esummit.setting.production')

app = Celery("esummit")
app.config_from_object("django.conf:settings", namespace="CELERY")
import user.tasks
app.autodiscover_tasks()