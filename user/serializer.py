from rest_framework import serializers
from .models import querry


class QuerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = querry
        include=["name","email","phone_number","message"]
        