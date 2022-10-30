
from msilib.schema import Class
from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    image=models.ImageField(upload_to='services/')

class EventCoordinator(models.Model):
    name = models.CharField(max_length=100, verbose_name="Coordinator Name")
    email = models.EmailField(max_length=100, verbose_name="Email Id")
    phone_number = models.IntegerField(verbose_name="Phone Number")

    class Meta:
        """
        Meta class for EventCoordinator
        """
        verbose_name_plural = 'Event Coordinators'


    def __str__(self):
        return self.name
