from django.shortcuts import render
from .serializer import StartupUser, ProffUser, StudentUser, CAUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
# Create your views here.

class LoginApiView(APIView):
  # def get_serializer_class(self):
  #   if self.request.esummit_id=='stp':
  #     return StartupUser
  #   if self.request.esummit_id=='stu':
  #     return StudentUser
  #   if self.request.esummit_id=='CAP':
  #     return CAUser
  #   if self.request.esummit_id=='prf':
  #     return ProffUser
     
  
  def post(self, request):
    data = request.data
  
    password = data.get('password', None)
    esummit_id = data.get('esummit_id', None)
    professional_tag=''
    student= "" 
    print(student)
    
    if not esummit_id:
        return Response('Esummit_id cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
    if not password:
        return Response('Password cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
    print(esummit_id.find("stu"))
    if esummit_id:
      if (esummit_id.find("stp")!=-1):
         student = StartupUser.objects.all().filter(esummit_id=esummit_id)
         professional_tag='stp'    
      elif(esummit_id.find("CAP")!=-1):
         student = CAUser.objects.all().filter(esummit_id=esummit_id)
         professional_tag='CAP'
      elif(esummit_id.find("stu")!=-1):
          student = StudentUser.objects.all().filter(esummit_id=esummit_id)
          professional_tag='stu'
      elif(esummit_id.find("prf")):
          student = ProffUser.objects.all().filter(esummit_id=esummit_id)
          professional_tag='prf'
    print("trys",student[0].password)
    if student:
        if check_password(student[0].password,password):
          r=str(student[0].authToken) 
          return Response({'token': r , 'role': professional_tag}, status=status.HTTP_200_OK)
    
    return Response({'error_msg: Username or password not found!'}, status=status.HTTP_404_NOT_FOUND) 
          
          
            
                                                                             
          
          
      
    # if student.DoesNotExist:
    #    return Response({'error_msg: Username not found!'}, status=status.HTTP_404_NOT_FOUND)
        # except student.DoesNotExist:
        #     return Response({'error_msg: Username not found!'}, status=status.HTTP_404_NOT_FOUND)

        
      # user = authenticate(email=email, password=password)
    
   
   


    # if user is not None:
    #     return Response({'token': Token.key, 'role': professional_tag}, status=status.HTTP_200_OK)
      
    # return Response({'error_msg': 'Password does not match'}, status=status.HTTP_403_FORBIDDEN)
    
#  def LoginData(request):
#     if request.esummit_id=='stp':
#      serializer = StartupUser(data={"esummit_id":request.data.get("esummit_id"),"password":request.data.get("password")})
#      return(serializer.data)
#     if request.esummit_id=='stu':
#      serializer = StudentUser(data={"esummit_id":request.data.get("esummit_id"),"password":request.data.get("password")})
#      return(serializer.data)
#     if request.esummit_id=='CAP':
#      serializer = ProffUser(data={"esummit_id":request.data.get("esummit_id"),"password":request.data.get("password")})
#      return(serializer.data)
#     if request.esummit_id=='prf':
#      serializer = CAUser(data={"esummit_id":request.data.get("esummit_id"),"password":request.data.get("password")})
#      return(serializer.data)


# def LoginView(request,esummit_id,password):
   
#   if not esummit_id:
#         return Response('Esummit_id cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
#   if not password:
#         return Response('Password cannot be empty!', status=status.HTTP_400_BAD_REQUEST)


#   if esummit_id:
  
#    if request.data.get('esummit_id') == 'CAP':
#      student = student.object.get(esummit_id=esummit_id)
#      professional_tag='CAP'
#    if request.data.get('esummit_id') == 'prf':
#      student = student.object.get(esummit_id=esummit_id)
#      professional_tag='prf'
#    if request.data.get('esummit_id') == 'stu':
#      student = student.object.get(esummit_id=esummit_id)
#      professional_tag='stu'
#    if request.data.get('esummit_id') == 'stp':
#      student = student.object.get(esummit_id=esummit_id)
#      professional_tag='stp'
#    if student:
#         if check_password(password=password):
#           return Response({'token': Token.key, 'role': professional_tag}, status=status.HTTP_200_OK)
#    else:
#     return Response({'error_msg: Username not found!'}, status=status.HTTP_404_NOT_FOUND)  
          