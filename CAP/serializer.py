from CAP.models.submission import Submission,Goodies
from CAP.models.tasks import Task, TaskStatus
from CAP.models.users import CapUsers
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapUsers
        fields = ['email', 'password','gender','phone_number','college','state','city','studyYear','fullname']
        
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta :
        model =  TaskStatus
        fields = ['taskId','images','esummitId']

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
        
class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '_all_'

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= CapUsers
        fields=['taskCompleted','totalpoints','fullname','college','studyYear']