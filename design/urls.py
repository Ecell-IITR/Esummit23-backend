from django.urls import path, include
from .views import colors
from . import views

urlpatterns = [

  
    path('colors/', colors.as_view()),


]