from django.urls import path, include
from . import views

urlpatterns = [

  
    path('colors/', views.colors.as_view()),


]
