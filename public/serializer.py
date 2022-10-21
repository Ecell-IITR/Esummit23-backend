from rest_framework import serializers
from . models import Speakers
from rest_framework import serializers


class Speakerserializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        exclude = ['created', 'updated']



