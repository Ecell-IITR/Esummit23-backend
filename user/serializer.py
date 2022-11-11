from rest_framework import serializers
from .models.role.startup import StartupUser
from .models.role.student import StudentUser
from .models.role.proff import ProffUser
from .models.role.ca import CAUser
from .models.querry import Querry


class QuerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Querry
        fields = ["name", "email", "phone_number", "message"]


class EventStartpuUser(serializers.ModelSerializer):
    class Meta:
        model = StartupUser
        fields = ["startup_name", "email", "phone_number", "esummit_id"]


class EventStudentUser(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ["name", "email", "phone_number", "esummit_id"]


class EventProffUser(serializers.ModelSerializer):
    class Meta:
        model = ProffUser
        fields = ["name", "email", "phone_number", "esummit_id"]


class CAUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAUser
        exclude=['payment','taskAssigned','taskCompleted','esummit_id','created','updated','authToken','points']
