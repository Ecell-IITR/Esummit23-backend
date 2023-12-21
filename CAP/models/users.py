from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
import jwt
from django.contrib.auth.hashers import make_password
SECRET_KEY = '7o9d=)+(f-chzvhcr#*(dc6k!#8&q2=)w5m4a+d$-$m&)hr4gh'

class CapUsers(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    fullname = models.CharField(max_length=50, verbose_name="Name",default="")
    email = models.EmailField(db_index=True, max_length=100, unique=True, verbose_name="Email",default="")
    gender = models.CharField(max_length=10, verbose_name="gender", choices=GENDER_CHOICES,default="")
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(regex="^[6-9]\d{9}$",
                           message="Phone Number Not Valid",)
        ],
        blank=True,
        null=True,
        verbose_name="Phone Number")
    college= models.CharField(max_length=100, verbose_name="College",default="")
    state= models.CharField(max_length=100, verbose_name="State",default="")
    city= models.CharField(max_length=100, verbose_name="City",default="")
    studyYear = models.CharField(max_length=10,verbose_name="YearofStudy",default="")
    totalpoints=models.IntegerField(default=0)
    taskCompleted=models.IntegerField(default=0)
    esummitId = models.CharField(max_length=100,verbose_name="EsummitId",default="")
    refferedby = models.CharField(max_length=100,verbose_name="RefferedBy",default="")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=100,verbose_name="password",default="nopassward"+str(esummitId))
    jwt_secret = SECRET_KEY
    jwt_algorithm = "HS256"
    authToken = models.CharField(max_length=1000, blank=True, null=True,default="")

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

            self.password = make_password(self.password)

        self.updated = timezone.now()

        self.authToken = jwt.encode({"email": self.email, "password": self.password,
                                    "updated": str(self.updated)}, self.jwt_secret, algorithm=self.jwt_algorithm)

        if not self.esummitId:
            # getting a non-repeating number
            unique_id = CapUsers.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummitId = 'ES24'+'CAP' + \
                str((unique_value + 1) * 31)
        

        return super(CapUsers, self).save(*args, **kwargs)
    
    def _str_(self):
        return self.fullname

    class Meta:
        """
        Meta class for Doctor
        """
        verbose_name_plural = "Capusers"