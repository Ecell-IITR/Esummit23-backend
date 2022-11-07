from rest_framework import serializers

from .models import querry 

class QuerrySerializer(serializers.Serializer):
    class Meta:
        model = querry.Querry
        execlude=["name","email","phone_number","message"]
    def create(self,validated_data):
            return querry.Querry.objects.create(**validated_data)
        