from rest_framework.response import Response
from user.models.otp import OTP
import pyotp
import smtplib
from rest_framework.generics import GenericAPIView
from .serializer import otpSerializer
from time import time
from .serializer import QuerrySerializer, CAUserSerializer, StudentUserSerializer, ProffUserSerializer, StartupUserSerializer, PearsonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import StartupUser, ProffUser, StudentUser, CAUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from .models.person import person

# Create your views here.


class LoginApiView(APIView):

    def post(self, request):
        data = request.data

        password = data.get('password', None)
        esummit_id = data.get('esummit_id', None)
        professional_tag = ''
        user = False

        if not password:
            return Response('Password cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        if not esummit_id:
            return Response('Esummit_id cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        else:
            if (esummit_id.find("stp") != -1):
                user = StartupUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'stp'
            elif(esummit_id.find("CAP") != -1):
                user = CAUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'ca'
            elif(esummit_id.find("stu") != -1):
                user = StudentUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'stu'
            elif(esummit_id.find("prf")):
                user = ProffUser.objects.all().filter(esummit_id=esummit_id)
                professional_tag = 'prf'

        if user:
            if check_password(password, user[0].password):

                at = str(user[0].authToken)

                return Response({"n": user[0].full_name, 'at': at, 'role': professional_tag}, status=status.HTTP_200_OK)

        return Response({'error_msg': 'check the credentials'}, status=status.HTTP_404_NOT_FOUND)


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
        print(db_entry.is_valid(), db_entry.errors)
        if db_entry.is_valid():

            db_entry.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def SignupView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        email = request.data["user"]['email']
        name = request.data["user"]['name']

        if person.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        saver = False
        db_entry = ""
        db_entry_person = PearsonSerializer
        data = request.data["user"]
        userType = request.data.get('UserType')
        if userType == 'ca':
            try:
                data["referred_by"] = ""
                db_entry = CAUserSerializer(data=data)
                db_entry.is_valid(raise_exception=True)
                saver = db_entry.save()
                data2 = {"email": email, "name": name, "ca": saver}
                db_entry_person = PearsonSerializer(data=data2)
                db_entry_person.is_valid(raise_exception=True)
                db_entry_person.save()
            except:
                return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)
        if userType in ('student', "proff", "stp"):

            try:
                data["referred_by"] = request.data["referred_by"]

            except:
                data["referred_by"] = " "

            db_entry = StudentUserSerializer(data=data)

            if userType == 'proff':
                db_entry = ProffUserSerializer(data=data)

            if userType == 'stp':

                db_entry = StartupUserSerializer(data=data)

            if db_entry.is_valid(raise_exception=True):
                saver = db_entry.save()
                data2 = {"email": email, "name": name}
                if userType == 'student':
                    data2["student"] = saver
                if userType == 'proff':
                    data2["proff"] = saver
                db_entry_person = PearsonSerializer(data=data2)
                db_entry_person.is_valid(raise_exception=True)
                db_entry_person.save()

            else:
                return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)
            try:

                user = CAUser.objects.filter(esummit_id=data["referred_by"])[0]

                user.save()
            except:
                pass
        message = "Dear "+"<b>"+saver.full_name+"</b>" + \
            " account created your esummit id is "+"<b>"+saver.esummit_id+"</b>"
        send_mail('esummit account created', "", 'from@example.com', [
                  saver.email], fail_silently=False, html_message=message)
        return Response({"name": saver.full_name, "e_id": saver.esummit_id, "at": saver.authToken}, status=status.HTTP_201_CREATED)

        # return Response(status=status.HTTP_400_BAD_REQUEST)
