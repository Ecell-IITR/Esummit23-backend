from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,GenericAPIView
from .serializer import EventMiniSerializer,EventSerializer
from .models import Event
from rest_framework import status

# Create your views here.
class EventListView(ListAPIView):
    serializer_class = EventMiniSerializer
    queryset = Event.objects.all()
class EventSingleView(APIView):
        serializer_class = EventSerializer
        def get(self, request, event_name):
            # print(event_type, event_name)
            final_data = {"No Such Event with that Type and Event Name"}
            final_status = status.HTTP_404_NOT_FOUND
            
            event = Event.objects.filter(event_name=event_name)

            if event:
                eventSerializer = EventSerializer(
                    event, many=True)
                final_data = eventSerializer.data
                final_status = status.HTTP_200_OK
            return Response(data=final_data, status=final_status)








