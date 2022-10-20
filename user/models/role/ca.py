from user.models.abstarct import AbstractProfile
from events.models import Services
from django.db import models

class CAUser(AbstractProfile):
    collage = models.CharField(max_length=50, verbose_name="Collage")
    points = models.IntegerField(default=0)
    branch = models.CharField(max_length=50, verbose_name="Branch")
    year = models.CharField(max_length=10, verbose_name="Year")
    city = models.CharField(max_length=50, verbose_name="City")
    state = models.CharField(max_length=50, verbose_name="State")
    taskAssigned = models.ManyToManyField(Services, verbose_name="Task Assigned")
    esummit_id = models.CharField(max_length=20, unique=True, db_index=True)
    def save(self, *args, **kwargs):
        professional_tag = "stup"

        if not self.esummit_id:
            # getting a non-repeating number
            unique_id = StartupUser.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES21'+professional_tag + \
                str((unique_value + 1) * 31)
    