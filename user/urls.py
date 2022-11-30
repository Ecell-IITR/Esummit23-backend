from django.urls import path,include
from .views import LoginApiView

urlpatterns = [
  path('login', LoginApiView.as_view(), name='Loginview'),
  
]