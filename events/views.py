from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,GenericAPIView
from .serializer import EventMiniSerializer,EventSerializer
from .models import Event
from rest_framework import status

# Create your views here.
class EventListView(ListAPIView):
    serializer_class = EventMiniSerializer
    queryset = Event.objects.all()
class EventSingleView(GenericAPIView):
    serializer_class = EventSerializer
    def get(self,request):
        try :
            print(request.data['name'])
            resData=Event.objects.filter(event_name=request.data['name'])
            
            serializer = EventSerializer(resData)
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"Event not found"},status=status.HTTP_404_NOT_FOUND)









