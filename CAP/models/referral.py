from django.db import models
from CAP.models.users import CapUsers

class Referral(models.Model):
    referrer=models.ForeignKey(CapUsers, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=50,unique=True)
    link_clicks=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.referrer.fullname}\'s referral : {self.referral_code}'
