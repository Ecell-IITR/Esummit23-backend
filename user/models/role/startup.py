from user.models.abstarct import AbstractProfile
from events.models import Services
from django.db import models

class StartupUser(AbstractProfile):
    startup_name = models.CharField(max_length=50, verbose_name="Startup Name")
    domain=models.CharField(max_length=50, verbose_name="Domain")
    category=models.CharField(max_length=50, verbose_name="Category")
    services=models.ManyToManyField(Services, verbose_name="Services")
    description=models.CharField(max_length=200, verbose_name="Description")
    esummit_id = models.CharField(max_length=20, unique=True, db_index=True)
    def save(self, *args, **kwargs):
        professional_tag = "stp"

        if not self.esummit_id:
            # getting a non-repeating number
            unique_id = StartupUser.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES23'+professional_tag + \
                str((unique_value + 1) * 31)
    