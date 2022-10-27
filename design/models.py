
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone




class Colors(models.Model):
    colourCategory=models.CharField(max_length=100)
    colourid=models.AutoField(primary_key=True)
    colourName=models.CharField(max_length=100)


    # date_event = models.DateField()
    # time_event = models.TimeField()
    created =  models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

def __str__ (self):
    return self.colourName

class meta():
    verbose_name_plural = "Colors"

def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Colors, self).save(*args, **kwargs)