from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
import jwt
from django.contrib.auth.hashers import make_password
import os

SECRET_KEY = '7o9d=)+(f-chzvhcr#*(dc6k!#8&q2=)w5m4a+d$-$m&)hr4gh'

if os.environ.get('ENVIRONMENT') == 'production':
    SECRET_KEY = "7o9d=)+(f-chzvhcr#*(dc6k!#8&q2=)w5m4a+d$-$m&)hr4gh"

class AbstractProfile(models.Model):

    full_name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(

    db_index=True, max_length=100, unique=True, verbose_name="Email")

    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(regex="^[6-9]\d{9}$",
                           message="Phone Number Not Valid",)
        ],
        blank=True,
        null=True,
        verbose_name="Phone Number")
    payment = models.IntegerField(default=0)

    referred_by = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField()

    updated = models.DateTimeField(auto_now=True)
    password = models.TextField()
    Services = models.ManyToManyField("events.Services", blank=True)
    jwt_secret = SECRET_KEY
    jwt_algorithm = "HS256"
    authToken = models.CharField(max_length=1000, blank=True, null=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

            self.password = make_password(self.password)

        self.updated = timezone.now()

        self.authToken = jwt.encode({"email": self.email, "password": self.password,
                                    "updated": str(self.updated)}, self.jwt_secret, algorithm=self.jwt_algorithm)

        return super(AbstractProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

