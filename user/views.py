from rest_framework.response import Response
from user.models.otp import OTP
import pyotp
import smtplib
from rest_framework.generics import GenericAPIView
from .serializer import otpSerializer
from time import time
from .serializer import QuerrySerializer, CAUserSerializer, StudentUserSerializer, ProffUserSerializer, StartupUserSerializer, PearsonSerializer, TeamSerializer
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
from .utils.auth import auth
from events.models import Services, EventRounds
from events.serializer import ServiceSerilizer
from user.tasks import send_feedback_email_task
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
                print(at[2:-1])
                print(at)

                return Response({"n": user[0].full_name, 'at': at[2:-1], 'role': professional_tag, "e_id": user[0].esummit_id}, status=status.HTTP_200_OK)

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

        detail = OTP.objects.filter(
            Email=request.data['Email'], Esummit_Id=request.data['Esummit_Id']).values()

        req = OTP.objects.get()
        d = int(time()*1000)

        d1 = req.date_expired
        d1 = (d1.timestamp()*1000)

        hours = abs((d-d1)/(1000*60*60))

        if len(detail) == 0:
            detail.is_vaild()
            detail.save()
            server.sendmail(sender_email, receiver_email, message)

        elif len(detail) == 1:
            if hours > 1:
                req.delete()
                db_entry = otpSerializer(data=data)
                db_entry.is_valid()
                db_entry.save()
                server.sendmail(sender_email, receiver_email, message)
            elif hours < 1:
                otp = req.Otp
                message = 'Your Otp is ' + str(otp)
                server.sendmail(sender_email, receiver_email, message)

            return Response("Successful", status=200)
        return Response("unsuccessful", status=400)


class QuerryView(APIView):

    def post(self, request):

        data = {"name": request.data.get("name"), "email": request.data.get(
            "email"), "phone_number": request.data.get("phone_number"), "message": request.data.get("message")}

        db_entry = QuerrySerializer(data=data)

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
        name = request.data["user"]['full_name']

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
                data2 = {"email": email, "name": name, "ca": saver.pk}
                db_entry_person = PearsonSerializer(data=data2)
                db_entry_person.is_valid(raise_exception=True)
                db_entry_person.save()

            except:
                return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)
        if userType in ('stu', "proff", "stp"):

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
                if userType == 'stu':
                    data2["student"] = saver.pk
                if userType == 'proff':
                    data2["proff"] = saver.pk
                db_entry_person = PearsonSerializer(data=data2)

                db_entry_person.is_valid()
                db_entry_person.save()

            else:
                return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)
            try:

                user = CAUser.objects.filter(esummit_id=data["referred_by"])[0]
                user.points = 50+user.points

                user.save()
            except:
                pass
        message = "Dear "+"<b>"+saver.full_name+"</b>" + \
            " account created your esummit id is "+"<b> "+saver.esummit_id+"</b>"
        # send_mail('esummit account created', "", 'from@example.com', [
        #           saver.email], fail_silently=False, html_message=message)
        mail = saver.email

        send_feedback_email_task.delay(
            mail, message, 'esummit account created'
        )
        return Response({"n": saver.full_name, "e_id": saver.esummit_id, "at": saver.authToken}, status=status.HTTP_201_CREATED)

        # return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def TeamSignupView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':

        # email = request.data["user"]['email']
        # name = request.data["user"]['name']
        Leader = auth(request.headers['Authorization'].split(' ')[1])
        if Leader == None:
            return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST)
        no = request.data["no_user"]
        no = int(no)
        if no > 4:
            return Response({"error": "Maximum 5 members allowed"}, status=status.HTTP_400_BAD_REQUEST)
        person_array = []

        for i in range(no):
            if person.objects.filter(email=request.data["users"][i]['email']).exists():
                person_array.append(person.objects.filter(
                    email=request.data["users"][i]['email'])[0])

            else:
                email = request.data["users"][i]['email']
                name = request.data["users"][i]['full_name']
                saver = False
                db_entry = ""
                db_entry_person = PearsonSerializer
                data = request.data["users"][i]

                data["referred_by"] = ""
                data["password"] = "esummit23"
                db_entry = StudentUserSerializer(data=data)

                if db_entry.is_valid():
                    saver = db_entry.save()
                    data2 = {"email": email, "name": name}
                    data2["student"] = saver.pk
                    db_entry_person = PearsonSerializer(data=data2)
                    if db_entry_person.is_valid():
                        db_entry_person.save()
                    else:
                        return Response({"Faliure": str(db_entry_person.errors)}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)

                message = "Dear "+"<b>"+saver.full_name+"</b>" + \
                    " account created your esummit id is "+"<b> "+saver.esummit_id+"</b>"
        # send_mail('esummit account created', "", 'from@example.com', [
        #           saver.email], fail_silently=False, html_message=message)
                mail = saver.email

                send_feedback_email_task.delay(
                    mail, message, 'esummit account created'
                )
                person_array.append(person.objects.filter(
                    email=request.data["users"][i]['email'])[0])
        person_array_pk = []
        for i in person_array:
            person_array_pk.append(i.pk)

        lser = person.objects.filter(email=Leader.email)[0]
        data3 = {"name": request.data["team_name"],
                 "event": request.data["event"],
                 "submission_text": request.data["submission_text"],
                 "leader": lser.pk,
                 "members": person_array_pk,
                 "number_of_members": no+1}

        db_entry_team = TeamSerializer(data=data3)

        if db_entry_team.is_valid():

            db_entry_team.save()

            sevice = Services.objects.filter(name=request.data["event"])[0]
            person_array.append(lser)
            for i in person_array:

                if i.ca:
                    print(i)
                    i.ca.Services.add(sevice.pk)
                if i.student:
                    i.student.Services.add(sevice.pk)
                if i.proff:
                    i.proff.Services.add(sevice.pk)

            return Response({"success": "team created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Faliure": str(db_entry_team.errors)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def UserServices(request):
    if request.method == 'GET' and request.headers['Authorization']:

        user = auth(request.headers['Authorization'].split(' ')[1])
        if user == None:
            return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            servicesOpted = user.Services.all()
            allServices = list(Services.objects.filter(is_verified=True))
            restServiceList = [
                i for i in allServices if i not in servicesOpted]

            data1 = ServiceSerilizer(restServiceList, many=True)
            data2 = ServiceSerilizer(servicesOpted, many=True)
            return Response({"opt": data2.data, "rest": data1.data}, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
