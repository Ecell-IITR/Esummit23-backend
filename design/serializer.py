from rest_framework import serializers
from rest_framework import serializers
from .models import Colors



class ColourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colors
        exclude = ['created', 'updated']














        