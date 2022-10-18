from django.urls import path, include
from .views import TeamEventView

urlpatterns = [
    path('Team', TeamEventView.as_view()),
]