from django.shortcuts import render
from rest_framework.response import Response
from user.serializer import LeaderboardSerializer
from .serializer import SubmissionSerializer, TaskAssignedSerializer
from user.models.role.ca import CAUser
from rest_framework import filters
from rest_framework.decorators import api_view
from user.models.abstarct import AbstractProfile
from user.utils.auth import auth
from rest_framework import status
from django.db.models import Max
# Create your views here.
@api_view(('GET', 'POST'))
def Leaderboard(request):
  if request.method == 'GET':
     AuthToken = request.headers['Authorization'].split(' ')[1]
     user = auth(AuthToken) 
     
     if user == None:
         return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST) 

     else : 
      leaderboard= CAUser.objects.all().order_by('-points')
      queryset = CAUser.objects.all().annotate(latest=Max(('points'))).order_by('-points','latest')[:1200]
      current_CA = auth(AuthToken)
      rank_counter = 1
      for ca in queryset:   
          
          if(rank_counter>1200):
            current_CA.rank = str("1200+")
          else:
            ca.rank=rank_counter
            rank_counter+=1
          ca.save()
      leaderboard= CAUser.objects.all().order_by('-points')[0:20] 
      serializer= LeaderboardSerializer(leaderboard, many=True)
     
      # if serializer.is_valid(raise_exception=True):
      #    serializer.save()
      return Response({"data": serializer.data})


@api_view(('GET','POST'))
def Submission(request):
  if request.method =='POST':
     data={}
    #  data["esummitId"]=request.data["esummitId"]
    #  print(data)
     
     try: 
       
          data = {"taskId": request.data.get("taskId"), "esummitId": request.data.get(
            "esummitId"), "images": request.data.get("images"), "points" : request.data.get("points")}
        
          db_entry = SubmissionSerializer(data=data)          
          db_entry.is_valid(raise_exception=True)
      
          db_entry.save()
          return Response(data={"success":"data submitted"}, status=status.HTTP_200_OK) 
             
     except:
         return Response({"Faliure": "failure"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(('GET','POST'))   
def TaskAssigned(request):
  if request.method=='GET' :
    
    AuthToken = request.headers['Authorization'].split(' ')[1]
    user = auth(AuthToken) 
    if user == None:
         return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST) 

    else :
          taskassigned= user.taskAssigned.all().order_by('task_id')
          serializer = TaskAssignedSerializer(taskassigned, many=True)
          queryset = CAUser.objects.all().annotate(latest=Max(('points'))).order_by('-points','latest')[:1200]
          data=serializer.data
          rank= 1
          for ca in queryset:   
            if(ca==taskassigned):
              break
            else : 
              rank +=1
            if(rank>1201):
             rank = str("1200+")
          
          points = [{ "points" : user.points , "rank" : rank}]
          
          return Response({"points": points ,"data": data})




