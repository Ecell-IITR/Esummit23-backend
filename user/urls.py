  
from django.urls import path, include
from .views import QuerryView ,loginView
from . import views
from django.urls import path,include
from .views import LoginApiView , SignupView
from user.views import OtpView

urlpatterns = [
  path('login', LoginApiView.as_view(), name='Loginview'),
  path("signup",SignupView,name="SignupView"),
    path('otp', OtpView.as_view()),
    path('querry', QuerryView.as_view()),]
