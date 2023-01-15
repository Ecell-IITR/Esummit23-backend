from CAP.models.submission import Submission,Goodies
from CAP.models.tasks import Task
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

class TaskAssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= ['task_id','desc','points','url']
        
