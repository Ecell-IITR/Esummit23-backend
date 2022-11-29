from django.urls import path, include
from .views import QuerryView ,loginView
from . import views
# from user.models.otp import OTP
from user.views import OtpView
urlpatterns = [
    path('otp', OtpView.as_view()),
]

urlpatterns = [
    path('querry', QuerryView.as_view()),
    path('login',loginView)
]