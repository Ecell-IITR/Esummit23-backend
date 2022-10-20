from django.urls import path, include
from .views import SpeakerEventView,TeamEventView

urlpatterns = [
    path('speakers', SpeakerEventView.as_view()),
    path('Team', TeamEventView.as_view()),
]
