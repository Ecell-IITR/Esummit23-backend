from django.shortcuts import render
from .serializer import QuerrySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
class QuerryView(generics.GenericAPIView):
    serializer_class=QuerrySerializer
    def post(self,request):
        try:
            
            data={"name":request.data["name"],"email":request.data["email"],"phone_number":request.data["phone_number"],"message":request.data["message"]  }
          
            db_entry=QuerrySerializer(data=data)
            print(db_entry)
            if db_entry.is_valid():
                db_entry.save()
                return Response("Successful", status=status.HTTP_200_OK);
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
      
        return Response("unsuccessful", status=status.HTTP_400_BAD_REQUEST);

# Create your views here.
