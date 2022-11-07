from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name="Task Name")
    # to be finish later
class Resources(models.Model):
    name = models.CharField(max_length=50, verbose_name="Resource Name")
    file = models.FileField(upload_to='capresources/')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
