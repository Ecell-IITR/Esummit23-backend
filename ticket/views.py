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
            "merchantId": RAZOR_KEY_ID,
            "amount": amount,
            "currency" : 'INR' ,
            "orderId" : razorpay_order["id"],
            }

        # save order Details to frontend
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)