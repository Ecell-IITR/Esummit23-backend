from rest_framework.response import Response
import pyotp


from .serializer import QuerrySerializer, CAUserSerializer, StudentUserSerializer, ProffUserSerializer, StartupUserSerializer, PearsonSerializer, TeamSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import StartupUser, ProffUser, StudentUser, CAUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from .models.person import person
from .utils.auth import auth
from events.models import Services, Event
from events.serializer import ServiceSerilizer
from user.tasks import send_feedback_email_task
from .utils.block import block_mail
from django.views.decorators.csrf import csrf_exempt
from ticket.models import Ticket, Payment

# Create your views here.


@csrf_exempt
@api_view(["POST", "GET"])
# Webhook_owner also helps identify the webhook target
def send_purchase_confirmation(request):
    

    data = request.data
    if (data['event'] != 'order.paid'):
        return Response({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
    
    email = data['payload']["payment"]["entity"]['notes']['email']
    phone = data['payload']["order"]["entity"]['notes']['phone']
    name = data['payload']["order"]["entity"]['notes']['name']
    amount = int(data['payload']["order"]["entity"]['amount'])/100
    person_obj = ""
    case2 = False
    if person.objects.filter(email=email).exists():
        person_obj = person.objects.get(email=email)
    else:
        student = StudentUser.objects.create(
            email=email, phone=phone, full_name=name, password="esummit@123")
        person_obj = person.objects.create(
            name=name, email=email, student=student
        )
        case2 = True

    payment_obj = Payment.objects.create(
        name=name, amount=amount, payment_id=data['payload']["payment"]["entity"]['id'], provider_order_id=data['payload']["payment"]["entity"]['order_id'])
    payment_obj.save()
    ticket_obj = Ticket.objects.create(
        Person=person_obj, payment=payment_obj, total_payment=amount, quantity=1)
    e_id = ""
    if person_obj.ca:
        e_id = person_obj.ca.esummit_id
    elif person_obj.student:
        e_id = person_obj.student.esummit_id
    elif person_obj.proff:
        e_id = person_obj.proff.esummit_id
    message = """Hi,<br>
Welcome to the world of entrepreneurship! Team Esummit, IIT Roorkee gladly welcomes you to the most remarkable entrepreneurial fest in North India. Watch out!<br>
Your Esummit ID: """ + e_id + """<br>
No. of tickets confirmed: """ + str(1) + """<br>
Payment mode: Online<br>
Event Dates: Feb 17 to Feb 19<br>
Venue: Campus, IIT Roorkee<br><br>

All the best for your prep. See you soon!"""
    if case2:
        message = """Hi,<br>
Welcome to the world of entrepreneurship! Team Esummit, IIT Roorkee gladly welcomes you to the most remarkable entrepreneurial fest in North India. Watch out!<br>
Your Esummit ID: """ + e_id + """<br>
No. of tickets confirmed: """ + str(1) + """<br>
Payment mode: Online<br>
Event Dates: Feb 17 to Feb 19<br>
Venue: Campus, IIT Roorkee<br><br>
your password is esummit@123<br>
All the best for your prep. See you soon!"""

    ticket_obj.save()
    person_obj.save()
    send_feedback_email_task.delay(
        email, message, "Esummit 2023 Ticket Confirmation"
    )
    return Response("Successful", status=status.HTTP_200_OK)


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
        print(esummit_id,password)
    
        if (esummit_id.find("STP") != -1):
            user = StartupUser.objects.all().filter(esummit_id=esummit_id)
            professional_tag = 'stp'
        elif(esummit_id.find("CAP") != -1):
            user = CAUser.objects.all().filter(esummit_id=esummit_id)
            professional_tag = 'ca'
        elif(esummit_id.find("STU") != -1):
            user = StudentUser.objects.all().filter(esummit_id=esummit_id)
            professional_tag = 'stu'
        elif(esummit_id.find("PRF") != -1):
            user = ProffUser.objects.all().filter(esummit_id=esummit_id)
            professional_tag = 'proff'
        print(user[0])
        if user:

            mail = user[0].email
            value= block_mail(mail,'')
            print(value)
            if value:
              return Response({'error_msg': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED) 
            else :
                if check_password(password, user[0].password):
                 at = str(user[0].authToken)

            print(user[0].password,check_password(password, user[0].password))
            if check_password(password, user[0].password):

                 return Response({"n": user[0].full_name, 'at': at[2:-1], 'role': professional_tag, "e_id": user[0].esummit_id}, status=status.HTTP_200_OK)

        return Response({'error_msg': 'check the credentials'}, status=status.HTTP_404_NOT_FOUND)


class OtpView(APIView):

    def post(self, request):

        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
        mail = request.data.get('email', None)
        if (block_mail(mail,'')):
              return Response({'error_msg': 'Blocked Credentials'}) 
        personi = person.objects.filter(email=mail)

        if len(personi) == 0:
            return Response({"error": "email not registered"}, status=400)
        else:
            personi = personi[0]
            personi.otp = otp
            personi.save()
            mail = personi.email
            message = "Your OTP is <b>" + otp + "</b>"
            send_feedback_email_task.delay(
                mail, message, 'Your OTP is '
            )
            return Response("Successful", status=200)


class VerifyView(APIView):
    def post(self, request):
        data = request.data
        
        otp = data.get('otp', None)
        email = data.get('email', None)
        if (block_mail(email,'')):
              return Response({'error_msg': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED) 
        password = data.get('password', None)
        if not otp:
            return Response('OTP cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response('Email cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response('Password cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
        else:
            personi = person.objects.filter(email=email)
            if len(personi) == 0:
                return Response("email not registered",status=400)
            else:
                personi = personi[0]
                print(personi.otp, otp)
                if personi.otp == otp:
                    user = ""
                    if personi.student:
                        user = personi.student
                        user.password = make_password(password)
                        user.save()
                    elif personi.ca:
                        user = personi.ca
                        user.password = make_password(password)
                        user.save()
                    elif personi.proff:
                        user = personi.proff
                        user.password = make_password(password)
                        user.save()
                    print(user.password)
                    personi.otp = ""
                    personi.save()
                    return Response("Password change Successful", status=200)
                else:
                    return Response("Wrong OTP", status=400)


class QuerryView(APIView):

    def post(self, request):

        data = {"name": request.data.get("name"), "email": request.data.get(
            "email"), "phone_number": request.data.get("phone_number"), "message": request.data.get("message")}
        if (block_mail(data.email)):
              return Response({'error_msg': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED) 
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
     if block_mail(email,''):
        return Response({'error': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)
        
     else :
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
                data["referred_by"] = ""

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
        message = "Congratulations " + "<b>"+saver.full_name+"</b>" + """Your IIT Roorkee E-Summit account has been created successfully.<br>
<br>
Your E-Summit ID is:<br>
 <b>"""+saver.esummit_id+"""</b><br>
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
        return Response({"n": saver.full_name, "e_id": saver.esummit_id, "at": saver.authToken}, status=status.HTTP_201_CREATED)

        # return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(('GET', 'POST'))
def TeamSignupView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        
        # email = request.data["user"]['email']
        # name = request.data["user"]['name']
        name_string = ""
        Leader = auth(request.headers['Authorization'].split(' ')[1])
        
        if Leader == None:
            return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST)
        name_string += Leader.full_name + " "
        no = request.data["no_user"]
        no = int(no)
        if no > 4:
            return Response({"error": "Maximum 5 members allowed"}, status=status.HTTP_400_BAD_REQUEST)
        person_array = []
        for i in range(no):
          if block_mail(request.data["users"][i]['email'],''):
            return Response({'error': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)  

        for i in range(no):
            name_string += request.data["users"][i]['full_name']+" "
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
                        message = str(db_entry_person.errors) + \
                            "<br><br><br>"+str(request.data)
                        send_feedback_email_task.delay(
                            "pranav_a@ece.iitr.ac.in", message, 'esummit account bug'
                        )
                        return Response({"Faliure": str(db_entry_person.errors)}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    message = str(db_entry_person.errors) + \
                        "<br><br><br>"+str(request.data)
                    send_feedback_email_task.delay(
                        "pranav_a@ece.iitr.ac.in", message, 'esummit account bug'
                    )
                    return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)

                message = "Dear "+"<b>"+saver.full_name+"</b>" + \
                    " account created your esummit id is "+"<b> " + \
                    saver.esummit_id+"</b> password is <b>Esummit23</b>"
         # send_mail('esummit account created', "", 'from@example.com', [
         #           saver.email], fail_silently=False, html_message=message)
                mail = saver.email
                person_array.append(person.objects.filter(
                    email=request.data["users"][i]['email'])[0])
                send_feedback_email_task.delay(
                    mail, message, 'esummit account created'
                )

        person_array_pk = []
        for i in person_array:
            person_array_pk.append(i.pk)

        lser = person.objects.filter(email=Leader.email)[0]

        person_array_pk.append(lser.pk)
        data3 = {"name": request.data["team_name"],
                 "event": request.data["event"],
                 "submission_text": request.data["submission_text"],
                 "submission_text2": request.data["submission_text2"],
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

                    i.ca.Services.add(sevice.pk)
                if i.student:
                    i.student.Services.add(sevice.pk)
                if i.proff:
                    i.proff.Services.add(sevice.pk)

            message = """Congratulations!<br>Your team <b>"""+str(request.data["team_name"]) + """</b> has been successfully registered for  IIT Roorkee E-Summit's <b>"""+request.data["event"]+""""</b>.<br><br>Your team members are: """ + \
                name_string + """<br><br>For further details about the event, click on the 'Events' tab on the website and proceed with your relevant event.<br><br>Thanks and Regards<br>Team E-Summit, IIT Roorkee"""
            mail = Leader.email

            send_feedback_email_task.delay(
                mail, message, 'esummit team registered'
            )
            return Response({"success": "team created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Faliure": str(db_entry_team.errors)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def NewTeamSignupView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':

        # email = request.data["user"]['email']
        # name = request.data["user"]['name']
        name_string = ""

        no = request.data["no_user"]
        no = int(no)

        if no > 5:
            return Response({"error": "Maximum 5 members allowed"}, status=status.HTTP_400_BAD_REQUEST)
        person_array = []
        for i in range(no):
          if block_mail(request.data["users"][i]['email'],''):
            return Response({'error_msg': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)  
        for i in range(no):
            name_string += request.data["users"][i]['full_name']+" "
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
                        message = str(db_entry_person.errors) + \
                            "<br><br><br>"+str(request.data)
                        send_feedback_email_task.delay(
                            "pranav_a@ece.iitr.ac.in", message, 'esummit account bug'
                        )
                        return Response({"Faliure": str(db_entry_person.errors)}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    message = str(db_entry_person.errors) + \
                        "<br><br><br>"+str(request.data)
                    send_feedback_email_task.delay(
                        "pranav_a@ece.iitr.ac.in", message, 'esummit account bug'
                    )
                    return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)

                message = "Dear "+"<b>"+saver.full_name+"</b>" + \
                    " account created your esummit id is "+"<b> " + \
                    saver.esummit_id+"</b> password is <b>Esummit23</b>"
         # send_mail('esummit account created', "", 'from@example.com', [
         #           saver.email], fail_silently=False, html_message=message)
                mail = saver.email
                person_array.append(person.objects.filter(
                    email=request.data["users"][i]['email'])[0])
                send_feedback_email_task.delay(
                    mail, message, 'esummit account created'
                )

        person_array_pk = []
        for i in person_array:
            person_array_pk.append(i.pk)

        data3 = {"name": request.data["team_name"],
                 "event": request.data["event"],
                 "submission_text": request.data["submission_text"],
                 "submission_text2": request.data["submission_text2"],
                 "leader": person_array[0].pk,
                 "members": person_array_pk,
                 "number_of_members": no+1}

        db_entry_team = TeamSerializer(data=data3)

        if db_entry_team.is_valid():

            db_entry_team.save()

            sevice = Services.objects.filter(name=request.data["event"])[0]

            for i in person_array:

                if i.ca:

                    i.ca.Services.add(sevice.pk)
                if i.student:
                    i.student.Services.add(sevice.pk)
                if i.proff:
                    i.proff.Services.add(sevice.pk)

            message = """Congratulations!<br>Your team <b>"""+str(request.data["team_name"]) + """</b> has been successfully registered for  IIT Roorkee E-Summit's <b>"""+request.data["event"]+""""</b>.<br><br>Your team members are: """ + \
                name_string + """<br><br>For further details about the event, click on the 'Events' tab on the website and proceed with your relevant event.<br><br>Thanks and Regards<br>Team E-Summit, IIT Roorkee"""
            mail = person_array[0].email
            if block_mail(mail,''):
             return Response('Blocked Credentials')
            send_feedback_email_task.delay(
                mail, message, 'esummit team registered'
            )
            return Response({"success": "team created"}, status=status.HTTP_201_CREATED)
        else:
            message = str(db_entry_team.errors) + \
                "<br><br><br>"+str(request.data)
            send_feedback_email_task.delay(
                "pranav_a@ece.iitr.ac.in", message, 'esummit account bug'
            )
            return Response({"Faliure": str(db_entry_team.errors)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def OtpSignupView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        email = request.data["user"]['email']
        name = request.data["user"]['full_name']
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
    
        if block_mail(email,''):
            return Response('Blocked Credentials')  
        if person.objects.filter(email=email).exists():
            personi = person.objects.get(email=email)
            personi.verified = False

            personi.otp = otp
            personi.save()
            message = "Your OTP is <b>" + otp + "</b>"
            send_feedback_email_task.delay(
                email, message, 'Your OTP for esummit account'
            )
            return Response({"message": "user intilized"}, status=status.HTTP_201_CREATED)
        saver = False
        db_entry = ""

        db_entry_person = PearsonSerializer
        data = request.data["user"]
        userType = request.data.get('type')
        db_entry = ""

        data["password"] = "esummit23"+str(otp)
        if userType == "stu":
            db_entry = StudentUserSerializer(data=data)
        elif userType == "proff":
            data["organisation_name"] = data["collage"]
            del data["collage"]
            db_entry = ProffUserSerializer(data=data)

        if db_entry.is_valid(raise_exception=True):
            saver = db_entry.save()
            data2 = {"email": email, "name": name}
            if userType == "stu":
                data2["student"] = saver.pk
            elif userType == "proff":
                data2["proff"] = saver.pk

            db_entry_person = PearsonSerializer(data=data2)

            db_entry_person.is_valid()
            personi = db_entry_person.save()
            personi.verified = False

            personi.otp = otp
            personi.save()
            message = "Your OTP is <b>" + otp + "</b>"
            send_feedback_email_task.delay(
                email, message, 'Your OTP for esummit account'
            )
            return Response({"message": "user intilized"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Faliure": str(db_entry.errors)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def OTPSignupVerify(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':

        data = request.data

        otp = data.get('otp', None)
        email = data.get('email', None)

        if block_mail(email,''):
            return Response({'error': 'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)  
        else :
         if not otp:
          return Response('OTP cannot be empty!', status=status.HTTP_400_BAD_REQUEST)
         if not email:



            return Response('Email cannot be empty!', status=status.HTTP_400_BAD_REQUEST)

         else:
            personi = person.objects.filter(email=email)
            if len(personi) == 0:
                return Response("email not registered", status=400)
            else:
                personi = personi[0]
                user = ""
                if personi.otp == otp:
                    personi.otp = ""
                    personi.verified = True
                    personi.save()
                    if personi.student:
                        user = personi.student
                    elif personi.proff:
                        user = personi.proff

                    at = user.authToken
                    data5 = {"n": user.full_name,
                             'at': at[2:-1], 'role': "stu", "e_id": user.esummit_id}
                    if personi.proff:
                        data5["role"] = "proff"
                    return Response(data5, status=status.HTTP_200_OK)

                else:
                    return Response("Wrong OTP", status=400)


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

