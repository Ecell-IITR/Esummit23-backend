
from django.shortcuts import render
from .models import Speakers
from .serializer import Speakerserializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response




class SpeakerEventView(ListAPIView):
    serializer_class = Speakerserializer
    queryset = Speakers.objects.all()


