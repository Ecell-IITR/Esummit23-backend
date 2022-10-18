from django.db import models
from email.policy import default



class Team(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(
        verbose_name='Designation', max_length=1000, blank=True)
    profile_image = models.ImageField(
        upload_to='Teams/', verbose_name='Team Image',  blank=True, null=True)
    team_mail = models.EmailField(
        verbose_name='Team Email', max_length = 254)
   
    # created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

        