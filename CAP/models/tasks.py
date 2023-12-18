from django.db import models
from django.utils import timezone
class Task(models.Model):  
    task_id = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000, verbose_name="description", default='null')
    points = models.IntegerField(default=0)
    format = models.CharField(max_length=50, verbose_name="Submission Format", default='null')
    url = models.CharField(max_length=200, default='null' )
    keywords = models.CharField(max_length=400, default='null')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.task_id)
    
    class Meta:
        """
        Meta class for Task
        """
        verbose_name_plural = "Tasks"

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        task=Task.objects.last()
        id=0
        if not self.task_id:
            if task:
             id=task.task_id+1
            self.task_id=id 

        

        self.updated = timezone.now()
        return super(Task, self).save(*args, **kwargs)

