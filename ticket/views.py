from django.shortcuts import render
import os
import razorpay
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Payment,Plan,Ticket
import json
from user.utils.auth import get_Person

# Get Razorpay Key id and secret for authorize razorpay client.
RAZOR_KEY_ID = os.getenv('RAZORPAY_KEY_ID', None)
RAZOR_KEY_SECRET = os.getenv('RAZORPAY_SECRET_KEY', None)
print(RAZOR_KEY_ID)
# Creating Razorpay Client instance.
razorpay_client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
# Create your views here.

@api_view(('POST',"GET"))
@csrf_exempt 
def RazorpayPaymentView(request):
    """
    APIView for Creating Razorpay Order.
    :return: list of all necessary values to open Razopary SDK
    """
    if request.method == 'POST':

        name = request.data.get('name', None)

        if not name :
            return Response({"error": "Please provide name"}, status=status.HTTP_400_BAD_REQUEST)
        

        # Create Order
        razorpay_order = razorpay_client.order.create(
            {"amount": int(1) *100, "currency": "INR", "payment_capture": "1"}
        )

        # Save the order in DB
        order = Payment.objects.create(
            name=name, amount="1", provider_order_id=razorpay_order["id"]
        )

        data = {
            "name" : name,
            "amount": 1,
            "currency" : 'INR' ,
            "orderId" : razorpay_order["id"],
            }

        # save order Details to frontend
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(('POST',"GET"))
def RazorpayCallback(request, *args, **kwargs):
    

        """
{'response': {'razorpay_payment_id': 'pay_L6OyjrdLtR9UBV', 'razorpay_order_id': 'order_L6OyNXuYRAmt03', 'razorpay_signature': '9fc4967d3d3ec7f00582f64bdf6b545e82f4f83482dbfd7dbf8c879d4e9251ee', 'status_code': 200}, 'razorpayPaymentId': 'pay_L6OyjrdLtR9UBV', 'razorpayOrderId': 'order_L6OyNXuYRAmt03', 'razorpaySignature': '9fc4967d3d3ec7f00582f64bdf6b545e82f4f83482dbfd7dbf8c879d4e9251ee'} 2
"""

  

        # geting data form request
        
        print(request)
        response = request.data["response"]
        #     print(response,2)
        # except:
        #     response = request.POST
        #     print(response,1)

        if "razorpay_signature" in response:

            data = razorpay_client.utility.verify_payment_signature(response)
            print(data)
            # if we get here Ture signature
            if data:
                payment_object = Payment.objects.get(provider_order_id = response['razorpay_order_id'])                # razorpay_payment = RazorpayPayment.objects.get(order_id=response['razorpay_order_id'])
                payment_object.status = PaymentStatus.SUCCESS
                payment_object.payment_id = response['razorpay_payment_id']
                payment_object.signature_id = response['razorpay_signature']          
                payment=payment_object.save()
                print(request.headers.get('Authorization'))
                Person=get_Person(request.headers.get('Authorization').split(' ')[1])
             
                # Creating Ticket
                ticket = Ticket.objects.create(
                    Person=Person,
                    name=payment_object.name,
                    payment=payment_object,
                    quantity=int(request.data.get('quantity')),
                    plan=Plan.objects.get(name=request.data.get('plan'))
                )
                ticket.save()
                return Response({'status': 'Payment Done'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Signature Mismatch!'}, status=status.HTTP_400_BAD_REQUEST)


        return Response({'error'}, status=status.HTTP_401_UNAUTHORIZED)

