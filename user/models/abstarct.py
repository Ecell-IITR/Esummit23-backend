from django.db import models
from django.utils import timezone

from django.contrib.auth.models import (AbstractUser)
from django.core.validators import RegexValidator



class AbstractProfile(AbstractUser):
    
    full_name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(
        db_index=True, max_length=100, verbose_name="EMail Id")
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        validators=[
            RegexValidator(regex="^[6-9]\d{9}$",
                           message="Phone Number Not Valid",)
        ],
        verbose_name="Phone Number")
    payment=models.IntegerField(default=0)
    referred_by = models.CharField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(AbstractProfile, self).save(*args, **kwargs)
    def __str__(self):
        return self.full_name

