from django.urls import path, include
from .views import EventListView , EventSingleView,Register, ServiceView

urlpatterns = [
    path('all', EventListView.as_view()),
    path('register', Register.as_view()),
    path('services', ServiceView.as_view()),
    path('<str:event_name>', EventSingleView.as_view()),
    
]
