
from django.urls import path
from .views import QuerryView, LoginApiView, SignupView, OtpView, TeamSignupView, UserServices, VerifyView, NewTeamSignupView,OtpSignupView, OTPSignupVerify ,send_purchase_confirmation,TeamecellOtpView,TeamecellVerifyView

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
    path('purchase_confirmation', send_purchase_confirmation),
    path('services', UserServices),
    path('teamotpverify',TeamecellVerifyView.as_view()),
    path('teamotp',TeamecellOtpView.as_view())]