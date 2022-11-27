from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from user.models.otp import OTP
import pyotp
import smtplib
from rest_framework.generics import GenericAPIView
from .serializer import otpSerializer
from time import time
from datetime import datetime
from .serializer import QuerrySerializer,CAUserSerializer,StudentUserSerializer,ProffUserSerializer,StartupUserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import querry 
from rest_framework.decorators import api_view
from .models.role.ca import CAUser
from django.core.mail import send_mail

class OtpView(GenericAPIView):
    serializer_class = otpSerializer
    def post(self,request):
            totp=pyotp.TOTP('base32secret3232')
            otp=totp.now()
            now = datetime.now()    
            key = "123"  # Generating Key
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            sender_email = 'vinaycool585@gmail.com'
            server.login(sender_email, "njoatccnzotfcmzt")
            receiver_email = request.data['Email']
            message= 'Your Otp is '+ str(otp)
            data={"Email":request.data['Email'],"Esummit_Id":request.data['Esummit_Id'],"Otp":otp} 
            db_entry= otpSerializer(data=data)
            print(db_entry)
            detail=OTP.objects.filter(Email=request.data['Email'],Esummit_Id=request.data['Esummit_Id']).values()
            print(detail)
            # d= (now.strftime("%m/%d/%Y, %H:%M:%S"))

            req=OTP.objects.get()
            
            d=int(time()*1000)
            print(d)
            d1=req.date_expired
            d1=(d1.timestamp()*1000)
            print(d1)
            hours=abs((d-d1)/(1000*60*60))
            print(hours)
            if len(detail)==0:
                detail.is_vaild()
                detail.save()
                server.sendmail(sender_email, receiver_email,message)
                print("errrttt")
            elif len(detail)==1:
                if hours>1:
                    req.delete()
                    db_entry= otpSerializer(data=data)
                    db_entry.is_valid()
                    db_entry.save()
                    server.sendmail(sender_email, receiver_email,message)
                    print("vhfjferir")
                elif hours<1:
                    otp=req.Otp
                    message= 'Your Otp is '+ str(otp)
                    server.sendmail (sender_email, receiver_email,message)
                    print("fhff")
                return Response("Successful", status=200)
            return Response("unsuccessful", status=400)



class QuerryView(generics.GenericAPIView):
    serializer_class=QuerrySerializer
    def post(self,request):
        
            
            data={"name":request.data.get("name"),"email":request.data.get("email"),"phone_number":request.data.get("phone_number"),"message":request.data.get("message")  }
          
            db_entry=QuerrySerializer(data=data)
  
            if db_entry.is_valid():
        
                db_entry.save()
                return Response( status=status.HTTP_201_CREATED);
            return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(('GET','POST'))
def loginView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
            db_entry=""
            data = request.data["user"]
            if request.data.get('UserType') == 'ca':
                
                data["referred_by"] = ""
                db_entry = CAUserSerializer(data=data)
                db_entry.is_valid(raise_exception=True)
                db_entry.save()
            if request.data.get('UserType') in ('student',"proff","stp"):
        
                try:
                    data["referred_by"] = request.data["referred_by"]
                    
                except:
                    data["referred_by"] = " "
                
                db_entry = StudentUserSerializer(data=data)
                
                if request.data.get('UserType') == 'proff':
                    db_entry=ProffUserSerializer(data=data)
                if request.data.get('UserType') == 'stp':
                    
                    db_entry=StartupUserSerializer(data=data)
                                
                db_entry.is_valid(raise_exception=False)
                
        
                db_entry.save()
                try:
                    print("hello")
                    user=CAUser.objects.filter(esummit_id=data["referred_by"])[0]
                    
                   
                    user.points=50+user.points
                    print(user.points)
                    user.save()
                except:
                    pass
            return Response(status=status.HTTP_201_CREATED)
        
            # return Response(status=status.HTTP_400_BAD_REQUEST)
