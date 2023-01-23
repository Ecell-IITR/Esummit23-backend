from unicodedata import name
from django.db import models
from django.utils import timezone
from user.models.role.ca import CAUser
from CAP.models.tasks import Task


# Create your models here.




class Leaderboard(models.Model):
    esummitId = models.CharField(max_length=50)
    taskassign =models.IntegerField(default=0,verbose_name='Task Assigned')
    taskcomplete= models.IntegerField(default=0, verbose_name='Task Completed')
    pointsearned = models.IntegerField(default=0, verbose_name='points')
    discount = models.IntegerField(default=0, verbose_name='Discount(%)')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        """
        Meta class for Leaderboard
        """
        verbose_name_plural = "Leaderboard"

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Leaderboard, self).save(*args, **kwargs)

class Submission(models.Model):
    taskId = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    images= models.ImageField(upload_to='Submission/',verbose_name='Submitted Images')
    esummitId = models.CharField(max_length=50,default='')
    check = models.BooleanField(default=False, verbose_name='Team Check')
    verify = models.BooleanField(default=False, verbose_name='Team Accepted')  
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.taskId)
    
    class Meta:
        """
        Meta class for Leaderboard
        """
        verbose_name_plural = "Submission"

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        if self.verify and self.check:
           user = CAUser.objects.get(esummit_id=self.esummitId)    
           user.points = user.points + self.points   
           self.points = 0
           task=Task.objects.filter(task_id=self.taskId)[0]
           user.taskCompleted.add(task.pk)   
           user.taskAssigned.clear()
           user.save()
           
         
          
                     
        self.updated = timezone.now()
        return super(Submission, self).save(*args, **kwargs)


class Goodies(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=500,verbose_name='Item',default='null')
    description = models.CharField(max_length=500,default='null')
    price = models.IntegerField(verbose_name='Price', default='null')
    def __str__(self):
        return self.name
    
    class Meta:
        """
        Meta class for Goodies
        """
        verbose_name_plural = "Goodies"

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Goodies, self).save(*args, **kwargs)






          