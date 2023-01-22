from .views import RazorpayPaymentView ,RazorpayCallback
from django.urls import path

urlpatterns = [
    path('razorpay', RazorpayPaymentView, name='razorpay'),
    path('razorpay/callback', RazorpayCallback, name='razorpay_callback'),
]