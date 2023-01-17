  
from django.urls import path
from .views import QuerryView, LoginApiView , SignupView ,OtpView,TeamSignupView,UserServices,VerifyView,NewTeamSignupView

urlpatterns = [
  path('login', LoginApiView.as_view(), name='Loginview'),
  path("signup",SignupView,name="SignupView"),
  path('otp', OtpView.as_view()),
  path('verify', VerifyView.as_view()),
  path('querry', QuerryView.as_view()),
  path('team_signup', TeamSignupView),
  path('team_signup/new', NewTeamSignupView),
  path('services', UserServices)]
