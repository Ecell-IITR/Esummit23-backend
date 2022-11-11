from django.shortcuts import render
from .serializer import QuerrySerializer,CAUserSerializer,StudentUserSerializer,ProffUserSerializer,StartupUserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import querry 
from rest_framework.decorators import api_view
from .models.role.ca import CAUser
class QuerryView(generics.GenericAPIView):
    serializer_class=QuerrySerializer
    def post(self,request):
        
            
            data={"name":request.data.get("name"),"email":request.data.get("email"),"phone_number":request.data.get("phone_number"),"message":request.data.get("message")  }
          
            db_entry=QuerrySerializer(data=data)
  
            if db_entry.is_valid():
        
                db_entry.save()
                return Response( status=status.HTTP_201_CREATED);
            return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(('GET','POST'))
def loginView(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = request.data["user"]
            if request.data.get('UserType') == 'ca':
                
                data["referred_by"] = ""
                db_entry = CAUserSerializer(data=data)
                db_entry.is_valid(raise_exception=True)
                db_entry.save()
            if request.data.get('UserType') in ('student',"proff","stp"):
        
                try:
                    data["referred_by"] = request.data["referred_by"]
                    
                except:
                    data["referred_by"] = " "
                
                db_entry = StudentUserSerializer(data=data)
                
                if request.data.get('UserType') == 'proff':
                    db_entry=ProffUserSerializer(data=data)
                if request.data.get('UserType') == 'stp':
                    
                    db_entry=StartupUserSerializer(data=data)
                                
                db_entry.is_valid(raise_exception=False)
        
                db_entry.save()
                try:
                    user=CAUser.objects.get(esummit_id=data["referred_by"])
                    user.points+=50
                    user.save()
                except:
                    pass
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        