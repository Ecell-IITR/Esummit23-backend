
from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    image=models.ImageField(upload_to='services/')

