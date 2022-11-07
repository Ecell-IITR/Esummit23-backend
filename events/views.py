from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .serializer import EventSerializer
from .models import Event

# Create your views here.
class EventView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()