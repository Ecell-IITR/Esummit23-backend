from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Querry(models.Model):
    name=models.CharField(max_length=50,verbose_name="Name")
    email=models.EmailField(db_index=True,max_length=100,verbose_name="EMail Id")
    phone_number=models.CharField(max_length=10,blank=True,null=True,validators=[RegexValidator(regex="^[6-9]\d{9}$",message="Phone Number Not Valid",)],verbose_name="Phone Number")
    message=models.TextField(max_length=1000,verbose_name="Message")
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    resolved_by=models.TextField(null=True,blank=True)
    resolved=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Querry, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        """
        Meta class for Querry
        """
        verbose_name_plural = "Queries"