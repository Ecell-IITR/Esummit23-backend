from django.urls import path, include
from .views import QuerryView

urlpatterns = [
    path('querry', QuerryView.as_view()),
]