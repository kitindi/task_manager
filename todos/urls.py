from django.urls import path 
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create_task", views.create_task, name="create-task"),
    path("delete_task/<int:id>", views.delete_task, name="delete-task"),
]
