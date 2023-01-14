from django.urls import path, include
from .views import Leaderboard

urlpatterns = [
    path('leaderboard', Leaderboard),   
]