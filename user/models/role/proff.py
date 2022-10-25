from user.models.abstarct import AbstractProfile
from events.models import Services
from django.db import models


class ProffUser(AbstractProfile):

    GENDER = (
        ('M', "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    organisation_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Organisation From")
    gender = models.CharField(max_length=1, blank=True,
                              null=True, verbose_name="Gender", choices=GENDER)
    industry = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Industry From")
    services = models.ManyToManyField(Services, verbose_name="Services")
    esummit_id = models.CharField(max_length=20, unique=True, db_index=True)
    referred_by = models.CharField(max_length=20,null=True,blank=True,default="")

    def save(self, *args, **kwargs):
        professional_tag = "prf"

        if not self.esummit_id:
            # getting a non-repeating number
            unique_id = ProffUser.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES23'+professional_tag + \
                str((unique_value + 1) * 31)
