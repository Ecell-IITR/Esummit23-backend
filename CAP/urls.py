from django.urls import path, include
from .views import Leaderboard, Submission, TaskAssigned

urlpatterns = [
    path('leaderboard', Leaderboard), 
    path('submission', Submission),
    path('taskassigned',TaskAssigned),
]