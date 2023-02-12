from django.shortcuts import render
import os
import razorpay
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Payment, Plan, Ticket
import json
from user.utils.auth import get_Person
from user.tasks import send_feedback_email_task
import csv
from user.models.person import person
from user.models.role.student import StudentUser
from user.tasks import send_feedback_email_task
# Get Razorpay Key id and secret for authorize razorpay client.
RAZOR_KEY_ID = os.getenv('RAZORPAY_KEY_ID', "rzp_live_U0W39W3I1yR00g")
RAZOR_KEY_SECRET = os.getenv('RAZORPAY_SECRET_KEY', "RndrTeCVPTxYTJxVt10S7KET")
# Creating Razorpay Client instance.
razorpay_client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
# Create your views here.


@api_view(('POST', "GET"))
@csrf_exempt
def RazorpayPaymentView(request):
    """
    APIView for Creating Razorpay Order.
    :return: list of all necessary values to open Razopary SDK
    """
    if request.method == 'POST':

        name = request.data.get('name', None)
        amount = request.data.get('amount', None)

        if not name:
            return Response({"error": "Please provide name"}, status=status.HTTP_400_BAD_REQUEST)

        # Create Order
        razorpay_order = razorpay_client.order.create(
            {"amount": int(amount) * 100, "currency": "INR",
             "payment_capture": "1"}
        )

        # Save the order in DB
        order = Payment.objects.create(
            name=name, amount=str(amount), provider_order_id=razorpay_order["id"]
        )

        data = {
            "name": name,
            "amount": int(amount),
            "currency": 'INR',
            "orderId": razorpay_order["id"],
        }

        # save order Details to frontend
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST', "GET"))
def RazorpayCallback(request, *args, **kwargs):

    response = request.data["response"]

    if "razorpay_signature" in response:

        data = razorpay_client.utility.verify_payment_signature(response)

        # if we get here Ture signature
        if data:
            # razorpay_payment = RazorpayPayment.objects.get(order_id=response['razorpay_order_id'])
            payment_object = Payment.objects.get(
                provider_order_id=response['razorpay_order_id'])
            payment_object.status = PaymentStatus.SUCCESS
            payment_object.payment_id = response['razorpay_payment_id']
            payment_object.signature_id = response['razorpay_signature']
            payment = payment_object.save()
            Person = get_Person(request.headers.get(
                'Authorization').split(' ')[1])

            # Creating Ticket
            ticket = Ticket.objects.create(
                Person=Person,
                name=payment_object.name,
                payment=payment_object,
                quantity=int(request.data.get('quantity')),
                plan=request.data.get('plan')
            )
            ticket.save()
            e_id = ""
            if Person.ca:
                e_id = Person.ca.esummit_id
            elif Person.student:
                e_id = Person.student.esummit_id
            elif Person.proff:
                e_id = Person.proff.esummit_id
            message = """Hi,<br>
Welcome to the world of entrepreneurship! Team Esummit, IIT Roorkee gladly welcomes you to the most remarkable entrepreneurial fest in North India. Watch out!<br>
Your Esummit ID: """ + e_id + """<br>
No. of tickets confirmed: """ + str(request.data.get('quantity')) + """<br>
Payment mode: Online<br>
Event Dates: Feb 17 to Feb 19<br>
Venue: Campus, IIT Roorkee<br><br>

All the best for your prep. See you soon!"""
            send_feedback_email_task.delay(
                Person.email, "Esummit 2023 Ticket Confirmation", message)
            return Response({'status': 'Payment Done'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Signature Mismatch!'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error'}, status=status.HTTP_401_UNAUTHORIZED)


def import_data(request):
    if request.method == 'POST':
        file = request.FILES['importData']
        decoded_file = file.read().decode('utf-8').splitlines()
        desc = request.POST["desc"]
        User = ""
        print(request.POST["user"])

        User = request.POST["user"]

        reader = csv.DictReader(decoded_file)

        for row in decoded_file:
            # print(row)
            data = row.split(",")
            print(data[0])
            per = ""
            stu = ""
            if not person.objects.filter(email=data[1]).exists():
                stu = StudentUser()
                stu.password = "123456"
                stu.full_name = data[0]
                stu.email = data[1]
                stu.phone = data[2]
                stu.save()
                per = person()
                per.student = stu
                per.email = data[1]
                per.name = data[0]
                per.save()
            else:
                
                per = person.objects.get(email=data[1])
                if per.student:
                    stu = per.student
                elif per.ca:
                    stu = per.ca    
                elif per.proff:
                    stu = per.proff
                
            ticket = Ticket()
            ticket.name = User
            ticket.Person = per
            ticket.quantity = 1
            ticket.plan = desc

            ticket.save()
            send_feedback_email_task(data[1], "Hi,<br>Welcome to the world of entrepreneurship! Team Esummit, IIT Roorkee gladly welcomes you to the most remarkable entrepreneurial fest in North India. Watch out!<br>Your Esummit ID: " +
                                     stu.esummit_id+"<br>No. of tickets confirmed: 1<br>Payment mode: Online<br>Event Dates: Feb 17 to Feb 19<br>Venue: Campus, IIT Roorkee<br><br>All the best for your prep. See you soon!", "Esummit 2023 Ticket Confirmation")

        # if file_format == 'CSV':
        #     imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
        #     result = employee_resource.import_data(dataset, dry_run=True)
        # elif file_format == 'JSON':
        #     imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
        #     # Testing data import
        #     result = employee_resource.import_data(dataset, dry_run=True)

        # if not result.has_errors():
        #     # Import now
            # employee_resource.import_data(dataset, dry_run=False)

    return render(request, r'import.html')
