# Add all your views here

from re import template
from django.forms import ModelForm, ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task


class AuthorisedTaskManager(LoginRequiredMixin):
    def get_queryset(self):
        return Task.objects.filter(deleted=False, user=self.request.user)


class UserLoginView(LoginView):
    template_name = "user_login.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "user_create.html"
    success_url = "/user/login/"


def session_storage_view(request):
    total_views = request.session.get("total_views", 0)
    request.session["total_views"] = total_views + 1
    return HttpResponse(f"Total views is {total_views} and user is {request.user}")


class GenericTaskDeleteView(AuthorisedTaskManager, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = "/tasks"


class GenericTaskDetailView(AuthorisedTaskManager, DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskCreateForm(ModelForm):
    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 10:
            raise ValidationError("Data too small")
        return title.upper()

    class Meta:
        model = Task
        fields = ["title", "description", "completed"]


class GenericTaskUpdateView(AuthorisedTaskManager, UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "task_update.html"
    success_url = "/tasks"


# Just like ListView which is used to create model,
# we can use CreateView to generate forms for the model
class GenericTaskCreateView(CreateView):
    # model = Task
    # fields = ("title", "description", "completed")
    form_class = TaskCreateForm
    template_name = "task_create.html"
    success_url = "/tasks"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Reason to introduce class based views - generic views
# Generic views are built for a generic purpose CRUD ops
# List all the tasks - create a generic ListView and pass Task as Model/QuerySet
class GenericTaskView(LoginRequiredMixin, ListView):
    queryset = Task.objects.filter(completed=False).filter(deleted=False)
    template_name = "tasks.html"
    context_object_name = "tasks"
    # Pagination Feature
    paginate_by = 5

    def get_queryset(self):
        search_term = self.request.GET.get("search")
        tasks = Task.objects.filter(completed=False).filter(
            deleted=False, user=self.request.user
        )
        if search_term:
            tasks = tasks.filter(title__icontains=search_term)
        return tasks


class TaskView(View):
    def get(self, request):
        search_term = request.GET.get("search")
        tasks = Task.objects.filter(completed=False).filter(deleted=False)
        if search_term:
            tasks = tasks.filter(title__icontains=search_term)
        return render(request, "tasks.html", {"tasks": tasks})

    def post(self, request):
        pass


class CreateTaskView(View):
    def get(self, request):
        return render(request, "task_create.html")

    def post(self, request):
        task_value = request.POST.get("task")
        task_obj = Task(title=task_value)
        task_obj.save()
        return HttpResponseRedirect("/tasks")


def tasks_view(request):
    search_term = request.GET.get("search")
    tasks = Task.objects.filter(completed=False).filter(deleted=False)
    if search_term:
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
