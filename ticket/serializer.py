from rest_framework import serializers
from .models import StatisticsParticipants

class StatsParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsParticipants
        exclude=("TimeEntryExit",)