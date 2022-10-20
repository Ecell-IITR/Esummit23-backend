from django.shortcuts import render
from .models import Speakers, team
from .serializer import Speakerserializer, teamSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class SpeakerEventView(ListAPIView):
    serializer_class = Speakerserializer
    queryset = Speakers.objects.all()

class teamEventView(ListAPIView):
    serializer_class = teamSerializer
    queryset = team.objects.all()