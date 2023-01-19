from .views import RazorpayPaymentView
from django.urls import path

urlpatterns = [
    path('razorpay', RazorpayPaymentView, name='razorpay'),
]