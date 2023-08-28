from django.contrib import admin
from django.urls import path
from tasks.views import (
    add_task_view,
    all_tasks_view,
    complete_task_view,
    completed_tasks_view,
    delete_task_view,
    tasks_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", tasks_view),
    # /add-task appends query params after ? => so add-task?... gets redirect to add add-task/?...
    # GET /add-task/?task=Get+some+veggies
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("complete_task/<int:index>/", complete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("all_tasks/", all_tasks_view),
]
