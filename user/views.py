
from rest_framework.response import Response
from user.models.otp import OTP
import pyotp
import smtplib
from rest_framework.generics import GenericAPIView
from .serializer import otpSerializer
from time import time

from .serializer import QuerrySerializer, CAUserSerializer, StudentUserSerializer, ProffUserSerializer, StartupUserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models.role.ca import CAUser

from django.shortcuts import render
from .serializer import StartupUser, ProffUser, StudentUser, CAUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password, make_password
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
        professional_tag = ''
        student = ""
        print(student)

        if not esummit_id:
            return Response('Esummit_id cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response('Password cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        print(esummit_id.find("stu"))
        if esummit_id:
            if (esummit_id.find("stp") != -1):
                student = StartupUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'stp'
            elif(esummit_id.find("CAP") != -1):
                student = CAUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'CAP'
            elif(esummit_id.find("stu") != -1):
                student = StudentUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'stu'
            elif(esummit_id.find("prf")):
                student = ProffUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'prf'
        print("trys", student[0].password)
        print(check_password(
            password, student[0].password), password, student[0].password)
        if student:
            if check_password(password, student[0].password):
                print("uo")

                r = str(student[0].authToken)
                print(r, "")
                return Response({'token': r, 'role': professional_tag}, status=status.HTTP_200_OK)

        return Response({'error_msg: Username or password not found!'}, status=status.HTTP_404_NOT_FOUND)


class OtpView(GenericAPIView):
    serializer_class = otpSerializer

    def post(self, request):
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
        key = "123"  # Generating Key
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        sender_email = 'vinaycool585@gmail.com'
        server.login(sender_email, "njoatccnzotfcmzt")
        receiver_email = request.data['Email']
        message = 'Your Otp is ' + str(otp)
        data = {"Email": request.data['Email'],
                "Esummit_Id": request.data['Esummit_Id'], "Otp": otp}
        db_entry = otpSerializer(data=data)
        print(db_entry)
        detail = OTP.objects.filter(
            Email=request.data['Email'], Esummit_Id=request.data['Esummit_Id']).values()
        print(detail)
        req = OTP.objects.get()
        d = int(time()*1000)
        print(d)
        d1 = req.date_expired
        d1 = (d1.timestamp()*1000)
        print(d1)
        hours = abs((d-d1)/(1000*60*60))
        print(hours)
        if len(detail) == 0:
            detail.is_vaild()
            detail.save()
            server.sendmail(sender_email, receiver_email, message)
            print("errrttt")
        elif len(detail) == 1:
            if hours > 1:
                req.delete()
                db_entry = otpSerializer(data=data)
                db_entry.is_valid()
                db_entry.save()
                server.sendmail(sender_email, receiver_email, message)
                print("vhfjferir")
            elif hours < 1:
                otp = req.Otp
                message = 'Your Otp is ' + str(otp)
                server.sendmail(sender_email, receiver_email, message)
                print("fhff")
            return Response("Successful", status=200)
        return Response("unsuccessful", status=400)


class QuerryView(APIView):

    def post(self, request):
        print(request.data)
        data = {"name": request.data.get("name"), "email": request.data.get(
            "email"), "phone_number": request.data.get("phone_number"), "message": request.data.get("message")}

        db_entry = QuerrySerializer(data=data)
        print(db_entry.is_valid(),db_entry.errors)
        if db_entry.is_valid():

            db_entry.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({"Faliure":str(db_entry.errors)},status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def SignupView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        saver=False
        db_entry = ""
        data = request.data["user"]
        if request.data.get('UserType') == 'ca':

            data["referred_by"] = ""
            db_entry = CAUserSerializer(data=data)
            db_entry.is_valid(raise_exception=True)
            saver=db_entry.save()
        if request.data.get('UserType') in ('student', "proff", "stp"):

            try:
                data["referred_by"] = request.data["referred_by"]

            except:
                data["referred_by"] = " "

            db_entry = StudentUserSerializer(data=data)

            if request.data.get('UserType') == 'proff':
                db_entry = ProffUserSerializer(data=data)
            if request.data.get('UserType') == 'stp':

                db_entry = StartupUserSerializer(data=data)
            
            if db_entry.is_valid():
                saver=db_entry.save()
                print(saver)
            else:
                return Response({"Faliure":str(db_entry.errors)},status=status.HTTP_400_BAD_REQUEST)
            try:
            
                user = CAUser.objects.filter(esummit_id=data["referred_by"])[0]

                user.save()
            except:
                pass
        print(saver.authToken)
        return Response({"name":saver.full_name,"e_id":saver.esummit_id,"at":saver.authToken},status=status.HTTP_201_CREATED)

        # return Response(status=status.HTTP_400_BAD_REQUEST)
