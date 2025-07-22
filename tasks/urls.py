from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, delete_task, dashboard, HiHowGreetings, CreateTask, ViewProject, TaskDetailView, UpdateTask

urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', employee_dashboard, name='user-dashboard'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('view_task/', ViewProject.as_view(), name='view-task'),
    path('task/<int:task_id>/details/',
         TaskDetailView.as_view(), name='task-details'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('dashboard/', dashboard, name='dashboard'),
    path('greetings/', HiHowGreetings.as_view(greetings='Hi Good Day!'), name='greetings')
]
