from .views import RazorpayPaymentView ,RazorpayCallback, import_data,Sent_data,StatsParticipants,AddForm
from django.urls import path

urlpatterns = [
    path('razorpay', RazorpayPaymentView, name='razorpay'),
    path('razorpay/callback', RazorpayCallback, name='razorpay_callback'),
    path('import_data', import_data, name='import_data'),
    path('Sent_data', Sent_data),
    path('stats',StatsParticipants, name='Statistics' ),
    path('add',AddForm, name='add' )
]