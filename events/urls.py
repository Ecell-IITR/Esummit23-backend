from django.urls import path, include
from .views import EventListView , EventSingleView

urlpatterns = [
    path('all', EventListView.as_view()),
    path('', EventSingleView.as_view()),
    
]
