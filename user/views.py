from django.shortcuts import render
from .serializer import QuerrySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
class QuerryView(generics.GenericAPIView):
    serializer_class=QuerrySerializer
    def post(self,request):
        
            
            data={"name":request.data.get("name"),"email":request.data.get("email"),"phone_number":request.data.get("phone_number"),"message":request.data.get("message")  }
          
            db_entry=QuerrySerializer(data=data)
            
            if db_entry.is_valid():
                print(db_entry.is_valid())
                db_entry.save()
                return Response( status=status.HTTP_201_CREATED);
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
      
        
# Create your views here.
