from django.shortcuts import render
import os
import razorpay
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Payment
import json

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


        # Take Order Id from frontend and get all order info from Database.
        # order_id = request.data.get('order_id', None)

        # Here We are Using Static Order Details for Demo.
        name = request.data.get('name', None)
        amount = request.data.get('amount', None)
        if not name or not amount:
            return Response({"error": "Please provide name and amount"}, status=status.HTTP_400_BAD_REQUEST)
        

        # Create Order
        razorpay_order = razorpay_client.order.create(
            {"amount": int(amount) *1, "currency": "INR", "payment_capture": "1"}
        )

        # Save the order in DB
        order = Payment.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )

        data = {
            "name" : name,
            "amount": amount,
            "currency" : 'INR' ,
            "orderId" : razorpay_order["id"],
            }

        # save order Details to frontend
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(('POST',"GET"))
def RazorpayCallback(request, *args, **kwargs):
    


  
  

        # geting data form request
        
        print(request)
        try:
            response = request.data
            print(response,2)
        except:
            response = request.POST
            print(response,1)

        # if "razorpay_signature" in response:

        #     # Verifying Payment Signature
        #     data = razorpay_client.utility.verify_payment_signature(response)

        #     # if we get here Ture signature
        #     if data:
        #         payment_object = Payment.objects.get(provider_order_id = response['razorpay_order_id'])                # razorpay_payment = RazorpayPayment.objects.get(order_id=response['razorpay_order_id'])
        #         payment_object.status = PaymentStatus.SUCCESS
        #         payment_object.payment_id = response['razorpay_payment_id']
        #         payment_object.signature_id = response['razorpay_signature']          
        #         payment_object.save()

        return Response({'status': 'Payment Done'}, status=status.HTTP_200_OK)
        #     else:
        #         return Response({'status': 'Signature Mismatch!'}, status=status.HTTP_400_BAD_REQUEST)

        # # Handling failed payments
        # else:
        #     error_code = response['error[code]']
        #     error_description = response['error[description]']
        #     error_source = response['error[source]']
        #     error_reason = response['error[reason]']
        #     error_metadata = json.loads(response['error[metadata]'])

        #     razorpay_payment = Payment.objects.get(provider_order_id=error_metadata['order_id'])
        #     razorpay_payment.payment_id = error_metadata['payment_id']
        #     razorpay_payment.signature_id = "None"
        #     razorpay_payment.status = PaymentStatus.FAILURE
        #     razorpay_payment.save()

        #     error_status = {
        #         'error_code': error_code,
        #         'error_description': error_description,
        #         'error_source': error_source,
        #         'error_reason': error_reason,
        #     }

        #     return Response({'error_data': error_status}, status=status.HTTP_401_UNAUTHORIZED)

