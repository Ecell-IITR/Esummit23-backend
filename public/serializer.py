from rest_framework import serializers
from . models import Speakers, team


class Speakerserializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        exclude = ['created', 'updated']


class teamSerializer(serializers.ModelSerializer):
    class Meta :
        model = team
        # fields= '__all__'
        exclude = ['created', 'updated']