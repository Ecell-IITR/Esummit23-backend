from email.policy import default
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from datetime import datetime, timedelta
# import zoneinfo

# Create your models here.
class OTP(models.Model):
    Email = models.EmailField()
    Esummit_Id= models.CharField(max_length=15)
    Otp = models.CharField(max_length=15)
    date_created = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(default=timezone.now()+timedelta(minutes=30))
         
