from django.db import models
from django.utils import timezone
from CAP.models.users import CapUsers

class Task(models.Model):  
    # STATUS_CHOICES = [
    #     ('LIVE', 'Live'),
    #     ('PEND', 'Pending'),
    #     ('VERI', 'Verifed'),
    #     ('EXPI', 'Expired')
    # ]
    
    # status=models.CharField(max_length=200,default='LIVE',choices=STATUS_CHOICES)
    task_id = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000, verbose_name="description", default='null')
    points = models.IntegerField(default=0)
    # format = models.CharField(max_length=50, verbose_name="Submission Format", default='null')
    # url = models.CharField(max_length=200, default='null' )
    # keywords = models.CharField(max_length=400, default='null')
    deadline=models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
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

class TaskStatus(models.Model): 
    STATUS_CHOICES = [
        ('LIVE', 'Live'),
        ('PEND', 'Pending'),
        ('VERI', 'Verifed'),
        ('EXPI', 'Expired'),
        ('NOTACC','Not accepted'),
    ]
    
    esummitId = models.CharField(max_length=100,verbose_name="EsummitId",default="")
    status=models.CharField(max_length=200,default='null',choices=STATUS_CHOICES)
    taskId=models.CharField(max_length=100,verbose_name="Esummitid",default="")
    images= models.ImageField(upload_to='Submission/',verbose_name='Submitted Images',null=True)
    check = models.BooleanField(default=False, verbose_name='Team Check')
    verify = models.BooleanField(default=False, verbose_name='Team Accepted') 
    # inspected=models.CharField(default='no')
    # taskassign=models.IntegerField(default=0)
    taskpoint=models.IntegerField(default=0,null=True)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    def _str_(self):
        return str(self.taskId)
    
    class Meta:
        """
        Meta class for Task
        """
        verbose_name_plural = "Tasks"
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        if not self.check:
            task=Task.objects.get(task_id=self.taskId)
            self.taskpoint=task.points
            

           
        if self.verify and self.check: 
           user = CapUsers.objects.get(esummitId=self.esummitId)    
           user.totalpoints = int(user.totalpoints) + self.taskpoint
           if self.taskpoint>0:
               user.taskCompleted = int(user.taskCompleted) + 1
           self.taskpoint=0
           user.save()
              
        self.updated = timezone.now()
        return super(TaskStatus, self).save(*args, **kwargs)