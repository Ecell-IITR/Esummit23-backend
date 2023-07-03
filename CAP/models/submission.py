from django.db import models
from django.utils import timezone
from CAP.models.tasks import Task
from user.models.role.ca import CAUser


class Submission(models.Model):
    task = models.ForeignKey(to=Task,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    images= models.ImageField(upload_to='Submission/',verbose_name='Submitted Images')
    user = models.ForeignKey(to=CAUser,related_name="submission",on_delete=models.CASCADE() )
    check = models.BooleanField(default=False, verbose_name='Team Check')
    verify = models.BooleanField(default=False, verbose_name='Team Accepted') 
    startTime = models.DateField()
    endTime = models.DateField() 
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name}-{self.task.name}"
    
    class Meta:
        """
        Meta class for Submission
        """
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        if self.verify and self.check:
            user = self.user
            user.points = user.points + self.points   
            self.points = 0
            task=self.task
            user.taskCompleted.add(task)   
            user.save()

        self.updated = timezone.now()
        return super(Submission, self).save(*args, **kwargs)


# class Goodies(models.Model):
#     id = models.AutoField(primary_key=True)
#     item = models.CharField(max_length=500,verbose_name='Item',default='null')
#     description = models.CharField(max_length=500,default='null')
#     price = models.IntegerField(verbose_name='Price', default='null')
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         """
#         Meta class for Goodies
#         """
#         verbose_name_plural = "Goodies"

#     def save(self, *args, **kwargs):
#         if not self.created:
#             self.created = timezone.now()

#         self.updated = timezone.now()
#         return super(Goodies, self).save(*args, **kwargs)
