from django.views import View

from tasks.models import Task

# from django.http.response import JsonResponse

# class TaskListView(View):
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "completed", "created_date"]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(deleted=False)
        data = TaskSerializer(tasks, many=True).data
        return Response({"tasks": data})
        # # TaskList without serializer
        # tasks = Task.objects.filter(deleted=False)
        # data = []
        # for task in tasks:
        #     data.append({"title": task.title})
        # return Response({"tasks": data})
