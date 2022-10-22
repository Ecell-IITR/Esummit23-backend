from unicodedata import name
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name="Task Name")
    # to be finish later