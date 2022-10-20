from django.shortcuts import render
from .models import Speakers,Team
from .serializer import Speakerserializer,TeamSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class SpeakerEventView(ListAPIView):
    serializer_class = Speakerserializer
    queryset = Speakers.objects.all()

class TeamEventView(ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()