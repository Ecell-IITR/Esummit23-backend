from django.shortcuts import render
from rest_framework.response import Response
from user.serializer import LeaderboardSerializer
from user.models.role.ca import CAUser
from rest_framework import filters
from rest_framework.decorators import api_view

# Create your views here.
@api_view(('GET', 'POST'))
def Leaderboard(request):
  if request.method == 'GET':
    leaderboard= CAUser.objects.all().order_by('-points')[0:20]  
   
    serializer= LeaderboardSerializer(leaderboard, many=True)
    
    return Response({"data": serializer.data})
    
   
