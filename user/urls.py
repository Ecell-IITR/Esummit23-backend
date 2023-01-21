
from django.urls import path
from .views import QuerryView, LoginApiView, SignupView, OtpView, TeamSignupView, UserServices, VerifyView, NewTeamSignupView, OtpSignupView, OTPSignupVerify

urlpatterns = [
    path('login', LoginApiView.as_view(), name='Loginview'),
    path("signup", SignupView, name="SignupView"),
    path('otp', OtpView.as_view()),
    path('otp_signup', OtpSignupView),
    path('otp_signup/verify', OTPSignupVerify),
    path('verify', VerifyView.as_view()),
    path('querry', QuerryView.as_view()),
    path('team_signup', TeamSignupView),
    path('team_signup/new', NewTeamSignupView),
    path('services', UserServices)]
