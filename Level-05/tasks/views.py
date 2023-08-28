# Add all your views here

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task

tasks = []
completed_tasks = []


def tasks_view(request):
    search_term = request.GET.get("search")
    # tasks = Task.objects.all()

    # Soft Deletion
    tasks = Task.objects.filter(completed=False).filter(deleted=False)
    if search_term:
        # title => match title
        # title__contains => match title containing search_term
        # title__icontains => match title containing search_term case insensitive
        tasks = tasks.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(request):
    task_value = request.GET.get("task")
    task_obj = Task(title=task_value)
    task_obj.save()
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, index):
    # Task.object.filter(id=index).delete()

    # Soft Deletion
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")


def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/tasks")


def completed_tasks_view(request):
    completed_tasks = Task.objects.filter(completed=True).filter(deleted=False)
    return render(request, "completed.html", {"tasks": completed_tasks})


def all_tasks_view(request):
    tasks = Task.objects.filter(completed=False).filter(deleted=False)
    completed_tasks = Task.objects.filter(completed=True).filter(deleted=False)
    return render(
        request, "all.html", {"tasks": tasks, "completed_tasks": completed_tasks}
    )
