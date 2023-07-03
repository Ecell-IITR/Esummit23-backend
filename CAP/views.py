from rest_framework.response import Response
from .models.tasks import Task
from user.serializer import CaLeaderboadSerializer
from .serializer import SubmissionSerializer, TaskAssignedSerializer
from user.models.role.ca import CAUser
from rest_framework.decorators import api_view
from user.utils.auth import auth
from rest_framework import status
from datetime import datetime


@api_view(('GET',))
def Leaderboard(request):
    if request.method == 'GET':
        AuthToken = request.headers['Authorization'].split(' ')[1]
        user = auth(AuthToken)

        if user == None:
            return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST)
        else:

            queryset = CAUser.objects.all().order_by('-points')
            rank_counter = 1
            for ca in queryset:
                ca.rank = rank_counter
                rank_counter += 1
                ca.save()
            serializer = CaLeaderboadSerializer(data=queryset[:20])
            return Response({"data": serializer.data})
    return Response({"error": "method not allowed"})


@api_view(('POST',))
def Submission(request):
    if request.method == 'POST':
        data = {}
        id = request.data.get("taskId")
  
        AuthToken = request.headers['Authorization'].split(' ')[1]
        user = auth(AuthToken)
        task = Task.objects.filter(id=id)
        if user == None:
            return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST)
        
        elif datetime.now()>=task.endTime:
            return Response({"error": "Date passed"}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            try:

                data = {"taskId": request.data.get("taskId"), "user": user.id, "images": request.data.get(
                    "images"), "points": request.data.get("points")}
                db_entry = SubmissionSerializer(data=data)
                db_entry.is_valid(raise_exception=True)

                db_entry.save()
                return Response(data={"success": "data submitted"}, status=status.HTTP_200_OK)

            except:
                return Response({"error": "submission failed pls try again"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', 'POST'))
def TaskAssigned(request):
    if request.method == 'GET':

        AuthToken = request.headers['Authorization'].split(' ')[1]
        user = auth(AuthToken)
        if user == None:
            return Response({"error": "Invalid Auth Token"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            
            task_assigned = Task.objects.all().exclude(id_in=user.taskCompleted.all())

            serializer = TaskAssignedSerializer(task_assigned, many=True)
            rank = user.rank

            data = serializer.data

            points = [{"points": user.points, "rank": rank}]

            return Response({"points": points, "data": data})
