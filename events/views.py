from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from . models import Team
from . serializer import TeamSerializer

class TeamEventView(ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
