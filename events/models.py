from django.db import models
from email.policy import default
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(
        verbose_name='Designation', max_length=1000, blank=True)
    profile_image = models.ImageField(
        upload_to='Teams/', verbose_name='Team Image')
    team_mail = models.EmailField(
        verbose_name='Team Email', max_length = 254)
    team_phone = models.CharField(
        verbose_name='Team pnumber', max_length=15, blank=True)
    team_twitter = models.CharField(
        verbose_name='Team twitter', max_length=120, blank=True)
    team_linkedin = models.CharField(
        verbose_name='Team linkedin', max_length=120, blank=True) 

    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)
   
    # created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

