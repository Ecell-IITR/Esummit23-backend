from rest_framework import serializers
from . models import Speakers,Team


class Speakerserializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        exclude = ['created', 'updated']
        

class TeamSerializer(serializers.ModelSerializer):

    class Meta :
        model = Team
        # fields= '__all__'
        exclude = ['created', 'updated']