from rest_framework import serializers
from .models.otp import OTP


class otpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        exclude = ["id","date_created" ,"date_expired"]
