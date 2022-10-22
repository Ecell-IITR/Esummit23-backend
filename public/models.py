
from django.db import models

from django.utils import timezone


class Speakers(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(
        verbose_name='Designation', max_length=1000, blank=True)
    profile_image = models.ImageField(
        upload_to='speakers/', verbose_name='Speaker Image')
    date_event = models.DateField()
    time_event = models.TimeField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Speakers, self).save(*args, **kwargs)

    class Meta:
        """
        Meta class for Speaker
        """
        verbose_name_plural = "Speakers"

class Team(models.Model):
    name = models.CharField(max_length=120)

    designation = models.CharField(
        verbose_name='Designation', max_length=1000, blank=True)

    profile_image = models.ImageField(
        upload_to='teams/', verbose_name='Team Image')

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
        
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Team, self).save(*args, **kwargs)
    class Meta:
        """
        Meta class for Team
        """
        verbose_name_plural = "teams" 
