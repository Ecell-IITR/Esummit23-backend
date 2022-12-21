from django.db import models
from .role.ca import CAUser
from .role.proff import ProffUser
from .role.student import StudentUser
from django.utils import timezone

class person(models.Model):
    leader_status=models.BooleanField(default=False)
    name=models.CharField(max_length=50,verbose_name="Name")
    email=models.EmailField(db_index=True,max_length=100,verbose_name="EMail Id")
    student=models.ForeignKey(StudentUser,on_delete=models.CASCADE,blank=True,null=True)
    ca=models.ForeignKey(CAUser,on_delete=models.CASCADE,blank=True,null=True)
    proff=models.ForeignKey(ProffUser,on_delete=models.CASCADE,blank=True,null=True)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        
        verbose_name_plural = "persons"