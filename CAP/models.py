from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name="Task Name")
    esummit_id = models.CharField(max_length=50)
    points = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    keywords = models.CharField(max_length=400)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    
