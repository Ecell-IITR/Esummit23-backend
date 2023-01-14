from . models import Submission, Task, Goodies
from rest_framework import serializers


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Submission
        exclude = ['created', 'updated']


class TaskSerializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        exclude = ['created', 'updated']


class GoodiesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Goodies
        exclude = ['created', 'updated']


