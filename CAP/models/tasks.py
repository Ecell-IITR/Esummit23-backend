from django.db import models
from django.utils import timezone



class Task(models.Model):  
    # task_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50, verbose_name="name", default='null')
    desc = models.TextField( verbose_name="description", default='null')
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

        self.updated = timezone.now()
        return super(Task, self).save(*args, **kwargs)

