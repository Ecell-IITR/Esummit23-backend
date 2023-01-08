
from django.shortcuts import render
from .serializer import ColourSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import Colors
 


class colors(ListAPIView):
    serializer_class = ColourSerializer
    queryset = Colors.objects.all()

