from django.urls import path, include
from .views import SpeakerEventView, teamEventView

urlpatterns = [
    path('speakers', SpeakerEventView.as_view()),
    path('team', teamEventView.as_view()),
    
]
