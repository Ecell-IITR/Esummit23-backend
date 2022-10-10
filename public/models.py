
from email.policy import default
from django.db import models
from django.utils import timezone


class Speakers(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(
        verbose_name='Designation', max_length=1000, blank=True)
    profile_image = models.ImageField(
        upload_to='speakers/', verbose_name='Speaker Image',  blank=True, null=True)
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

    def __str__(self):
        return self.name
# Create your models here.
