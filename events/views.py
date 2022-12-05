from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,GenericAPIView
from .serializer import EventMiniSerializer,EventSerializer
from .models import Event
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie




# Create your views here.
class EventListView(APIView):

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def get(self,request):
        serializer = EventMiniSerializer(
                    Event.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

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








