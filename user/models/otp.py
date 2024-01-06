from django.db import models
from django.utils import timezone

class OTP(models.Model):
    Email = models.EmailField()
    Esummit_Id= models.CharField(max_length=15)
    Otp = models.CharField(max_length=15)
    date_created = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(null=True, blank=True)

         
