from django.urls import path, include
from .views import SpeakerEventView


urlpatterns = [

    path('speakers/', SpeakerEventView.as_view()),
   


]
