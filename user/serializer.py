
from rest_framework import serializers
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser

class ProffUserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = ProffUser
       fields = ['email', 'password', 'esummit_id']

class CAUserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = CAUser
       fields = ['email', 'password', 'esummit_id' ]

class StudentUserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = StudentUser
       fields = ['email', 'password','esummit_id' ]

class StartupUserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = StartupUser
       fields = ['email', 'password', 'esummit_id' ]

