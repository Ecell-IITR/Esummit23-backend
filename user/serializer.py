from rest_framework import serializers

from .models.querry  import Querry

class QuerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Querry
        fields = ["name","email","phone_number","message"]
      