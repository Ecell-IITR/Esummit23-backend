from django.urls import path
<<<<<<< HEAD
from .views import QuerryView, LoginApiView,getfile, SignupView, OtpView, TeamSignupView, UserServices, VerifyView, NewTeamSignupView,OtpSignupView, OTPSignupVerify ,send_purchase_confirmation,TeamecellOtpView,TeamecellVerifyView

urlpatterns = [
    path('login', LoginApiView.as_view(), name='Loginview'),
    path('getca',getca),
    path('getabstract',getAbstractProfile),
    path('getstartup'getstartup),
    path('csv',getfile),
=======
from .views import QuerryView, LoginApiView,getfile,getperson,getproff,getca,getstartup, SignupView, OtpView, TeamSignupView, UserServices, VerifyView, NewTeamSignupView,OtpSignupView, OTPSignupVerify ,send_purchase_confirmation,TeamecellOtpView,TeamecellVerifyView

urlpatterns = [
    path('login', LoginApiView.as_view(), name='Loginview'),
    path('getfile',getfile),
    path('getperson',getperson),
    path('getproff',getproff),
    path('getca',getca),
    # path('getabstract',getAbstractProfile),
    path('getstartup',getstartup),
>>>>>>> 97db731ef501642e84552d439899a14c442e6837
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
