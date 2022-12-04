from django.urls import path, include
from .views import EventListView , EventSingleView

urlpatterns = [
    path('all', EventListView.as_view()),
    path('<str:event_name>', EventSingleView.as_view()),
    
]
