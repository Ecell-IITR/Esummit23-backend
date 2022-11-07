from django.urls import path, include
from .views import EventView

urlpatterns = [
    path('list', EventView.as_view()),
    
]
