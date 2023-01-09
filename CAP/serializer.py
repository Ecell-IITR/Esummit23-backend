from . models import Submission, Task, Goodies, Leaderboard
from rest_framework import serializers


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Submission
        exclude = ['created', 'updated']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        exclude = ['created', 'updated']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Goodies
        exclude = ['created', 'updated']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Leaderboard
        exclude = ['created', 'updated']