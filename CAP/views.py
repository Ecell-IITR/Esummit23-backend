from django.shortcuts import render
from rest_framework.response import Response
from user.serializer import LeaderboardSerializer
from .serializer import SubmissionSerializer, TaskAssignedSerializer,UserSerializer
from user.models.role.ca import CAUser
from rest_framework import filters
from rest_framework.decorators import api_view
from user.models.abstarct import AbstractProfile
from user.utils.auth import auth
from rest_framework import status
from django.db.models import Max
from CAP.models.users import CapUsers
from user.tasks import send_feedback_email_task
from django.db import Error

# Create your views here.

@api_view(["POST"])
def user_registration(request):
        email = request.data.get('email')
        name = request.data.get('fullname')
        if CapUsers.objects.filter(email=email).exists():
             return Response({"email": "email already registered"}, status=status.HTTP_400_BAD_REQUEST)
        # db_entry = ""

        # db_entry_person = CAPUserRegisterSerializer
        # data = request.data
        try:
                data = {"college": request.data.get("college"), "state": request.data.get("state"), "city" : request.data.get("city"),
                "studyYear" : request.data.get("studyYear"),"phone_number" : request.data.get("phoneNumber"), "gender" : request.data.get("gender"),
                "fullname" : request.data.get("fullname"),"email": request.data.get("email"),"password":request.data.get("password")}
                print("pass2")
                db_entry = UserSerializer(data=data)
                print("pass3")
                db_entry.is_valid(raise_exception=True)
                saver = db_entry.save()
                # message = "Dear "+"<b>"+saver.fullname+"</b>" + \
                # " account created your esummit id is "+"<b> "+saver.esummitId+"</b>"
                message = "Dear "+"<b>"+saver.fullname+"</b>" + \
                  " account created your esummit id is "+"<b> "+saver.esummitId+"</b>"
        # send_mail('esummit account created', "", 'from@example.com', [
        #           saver.email], fail_silently=False, html_message=message)
                message = "Congratulations " + "<b>"+saver.fullname+"</b>" + """Your IIT Roorkee E-Summit account has been created successfully.<br>
<br>
Your E-Summit ID is:<br>
 <b>"""+saver.esummitId+"""</b><br>
<br>
Visit our website esummit.in/dashboard and login to register for the E-Summit events.<br>
<br>
<br>
Thanks and Regards<br>
<br>
Team E-Summit, IIT Roorkee"""
                mail = saver.email

                send_feedback_email_task.delay(
                mail, message, 'esummit account created'
                )
                return Response({"n": saver.fullname, "e_id": saver.esummitId, "at": saver.authToken}, status=status.HTTP_201_CREATED)


                # return Response(data={"success":"data submitted"}, status=status.HTTP_200_OK) 
                # data2 = {"email": email, "name": name, "ca": saver.pk}
                # db_entry_person = CAPUserRegisterSerializer(data=data2)
                # db_entry_person.is_valid(raise_exception=True)
                # db_entry_person.save()


        except Error as e :
            print(e)
            return Response({"Faliure": "failure"}, status=status.HTTP_400_BAD_REQUEST)



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
          rank = user.rank
          
          data=serializer.data
          
          # rank= 1
          # for ca in queryset:   
          #   if(ca==taskassigned):
          #     break
          #   else : 
          #     rank +=1
          #   if(rank>1201):
          #    rank = str("1200+")
          
          points = [{ "points" : user.points , "rank" : rank}]
          
          return Response({"points": points ,"data": data})




