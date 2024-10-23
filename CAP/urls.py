from django.urls import path, include
from .views import Leaderboard, Submission, TaskAssigned,user_registration,Login,CapuserInfo,taskStats,track_referral_click,view_referrals

urlpatterns = [
    path('leaderboard', Leaderboard), 
    path('submission', Submission),
    path('taskassigned',TaskAssigned),
    path('register/', user_registration, name='user-registration'),
    path('login',Login),
    path('userinfo',CapuserInfo),
    path('taskstats',taskStats),
    path('track-referral/',track_referral_click,name='track-referral'),
    path('referrals/',view_referrals,name='view_referrals'),
    # path('taskassigned',taskAssigned)
   
]