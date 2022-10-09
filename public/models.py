from datetime import date
from django.db import models


class Speakers(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(
         verbose_name='Designation', max_length=1000, blank=True)
    profile_image = models.ImageField(
          upload_to='speakers/', verbose_name='Speaker Image',  blank=True, null=True)
    date_event = models.DateField()
    time_event = models.TimeField()
    def __str__(self):
            return self.name

    class Meta:
            """
            Meta class for Speaker
            """
            verbose_name_plural = "Speakers"

    def __str__(self):
            return self.name
# Create your models here.
