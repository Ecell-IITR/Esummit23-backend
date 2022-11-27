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