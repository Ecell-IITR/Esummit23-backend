from django.urls import path, include
from . import views
# from user.models.otp import OTP
from user.views import OtpView
urlpatterns = [
    path('otp', OtpView.as_view()),
]