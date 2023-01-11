from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name="Task Name")
    desc = models.CharField(max_length=1000, verbose_name="description")
    points = models.IntegerField(default=0)
    format = models.CharField(max_length=50, verbose_name="Submission Format")
    url = models.CharField(max_length=200 )
    keywords = models.CharField(max_length=400)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
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
    images= models.ImageField(upload_to='Submission/',verbose_name='Submitted Images')
    esummitId = models.CharField(max_length=50)
    check = models.BooleanField(default=False, verbose_name='Team Check')
    verify = models.BooleanField(default=False, verbose_name='Team Accepted')
    mlpoints = models.IntegerField(verbose_name='Points ML')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        """
        Meta class for Leaderboard
        """
        verbose_name_plural = "Submission"

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Submission, self).save(*args, **kwargs)


class Goodies(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=500,verbose_name='Item')
    description = models.CharField(max_length=500)
    price = models.IntegerField(verbose_name='Price')
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






          