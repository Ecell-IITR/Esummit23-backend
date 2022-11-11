from django.urls import path, include
from .views import QuerryView ,loginView

urlpatterns = [
    path('querry', QuerryView.as_view()),
    path('login',loginView)
]