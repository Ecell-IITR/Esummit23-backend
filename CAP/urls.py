from django.urls import path, include
from .views import Leaderboard, Submission, TaskAssigned,user_registration,Login,CapuserInfo,taskStats

urlpatterns = [
    path('leaderboard', Leaderboard), 
    path('submission', Submission),
    path('taskassigned',TaskAssigned),
    path('register/', user_registration, name='user-registration'),
    path('login',Login),
    path('userinfo',CapuserInfo),
    path('taskstats',taskStats),
    # path('taskassigned',taskAssigned)
   
]