from rest_framework import serializers
from .models import Speakers, Team


class Speakerserializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        exclude = ['created', 'updated']


class teamSerializer(serializers.ModelSerializer):
    class Meta :
        model = Team
        exclude = ['created', 'updated']