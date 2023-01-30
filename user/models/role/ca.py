from user.models.abstarct import AbstractProfile
from django.db import models
from CAP.models.tasks import Task
class CAUser(AbstractProfile):
    collage = models.CharField(max_length=50, verbose_name="College", default="IIT Roorkee")
    points = models.IntegerField(default=0)
    year = models.CharField(max_length=10, verbose_name="Year",blank=True,null=True)
    city = models.CharField(max_length=50, verbose_name="City",blank=True,null=True)
    state = models.CharField(max_length=50, verbose_name="State",blank=True,null=True)
    gender = models.CharField(max_length=10, blank=True,
                              null=True, verbose_name="Gender")
    taskAssigned = models.ManyToManyField(Task, verbose_name="Task Assigned", related_name='task_assigned',blank=True)
    taskCompleted = models.ManyToManyField(Task, verbose_name="Task Completed", related_name='task_completed',blank=True)
    esummit_id = models.CharField(max_length=40, unique=True, db_index=True)
    rank = models.IntegerField(default=0)
    @property
    def noOftaskCompleted(self):
     task_count = self.taskCompleted.count()
     return task_count 
    
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
        
        return super(CAUser, self).save(*args, **kwargs)

