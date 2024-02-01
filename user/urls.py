from django.urls import path

from .views import OtpSendNew, OtpVerifyNew ,QuerryView, LoginApiView,getfile, SignupView, OtpView, TeamSignupView, UserServices, VerifyView, NewTeamSignupView,OtpSignupView, OTPSignupVerify ,send_purchase_confirmation,TeamecellOtpView,TeamecellVerifyView,getabstract,getperson,getstartuser

urlpatterns = [
    path('login', LoginApiView.as_view(), name='Loginview'),
    # path('getfile',getfile),
    path('getstartupuser',getstartuser),
    # path('getperson',getperson),
    # path('getproff',getproff),
    # path('getca',getca),
    # path('getstartup',getabstract),
    path("signup", SignupView, name="SignupView"),
    path('otp', OtpView.as_view()),
    path('otp_signup', OtpSignupView),
    path('otp_signup/verify', OTPSignupVerify),
    path('verify', VerifyView.as_view()),
    path('querry', QuerryView.as_view()),
    path('team_signup', TeamSignupView),
    path('team_signup/new', NewTeamSignupView),
    path('purchase_confirmations', send_purchase_confirmation),
    path('services', UserServices),
    path('teamotpverify',TeamecellVerifyView.as_view()),
    path('teamotp',TeamecellOtpView.as_view()),
    path('login', LoginApiView.as_view(), name='Loginview'),
    path( 'otp_send_new/',  OtpSendNew),
    path( 'otp_verify_new/',  OtpVerifyNew),
    # path('getca',getca),
    
    # path('getstartup',getstartup),
    path('csv',getfile),
    ]
