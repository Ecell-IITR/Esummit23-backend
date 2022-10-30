from user.models.abstarct import AbstractProfile

from django.db import models
from CAP.models import Task
class CAUser(AbstractProfile):
    collage = models.CharField(max_length=50, verbose_name="Collage")
    points = models.IntegerField(default=0)
    branch = models.CharField(max_length=50, verbose_name="Branch")
    year = models.CharField(max_length=10, verbose_name="Year")
    city = models.CharField(max_length=50, verbose_name="City")
    state = models.CharField(max_length=50, verbose_name="State")
    taskAssigned = models.ManyToManyField(Task, verbose_name="Task Assigned", related_name='task_assigned')
    taskCompleted = models.ManyToManyField(Task, verbose_name="Task Completed", related_name='task_cmpleted')
    esummit_id = models.CharField(max_length=20, unique=True, db_index=True)
    def save(self, *args, **kwargs):
        ca_tag = "CAP"

        if not self.esummit_id:
            # getting a non-repeating number
            unique_id = CAUser.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES23'+ca_tag + \
                str((unique_value + 1) * 31)
    