from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import EventMiniSerializer,EventSerializer,ServiceSerilizer
from .models import Event , Services
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from user.utils.auth import auth



# Create your views here.
class EventListView(APIView):

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

class Register(APIView):
    def post(self, request):
        data = request.data
        headers = request.headers
        auth_token=headers['Authorization'].split(' ')[1]
        auth_token=auth_token[2:]
        auth_token=auth_token[:-1]
        
        
        user = auth(auth_token)
        
        try:
            if user:
                
                user.Services.add(Services.objects.get(name=data['event_name']))
            
                user.payment=int(data['payment'])+user.payment
                user.save()
                event= Event.objects.get(event_name=data['event_name'])
                round = event.event_rounds.all()
                add_round=""
                for i in round:
                    r=str(i)
                    
                    if r.find("1")>-1:
                     
                        add_round=i
                if "ca" in str(type(user)):
                    add_round.CAUser.add(user)
                elif "prf" in str(type(user)):
                    add_round.ProffUser.add(user)
                elif "std" in str(type(user)):
                    add_round.StudentUser.add(user)
                elif "stup" in str(type(user)):
                    add_round.StartupUser.add(user)
                return Response(data={"success":"Registered for the event sucessfully"}, status=status.HTTP_200_OK)
            else:
                return Response(data={"error":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(data={"error":"Service not found"}, status=status.HTTP_404_NOT_FOUND)

class ServiceView(APIView):
    def get(self,request):
        data = Services.objects.all()
        serializer = ServiceSerilizer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterDetail(APIView):
    def get(self,request):
        data = request.data
        headers = request.headers
        auth_token=headers['Authorization'].split(' ')[1]
        auth_token=auth_token[2:]
        auth_token=auth_token[:-1]
        user = auth(auth_token)
        if user:
            data = user.Services.all()
            serializer = ServiceSerilizer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"error":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)




