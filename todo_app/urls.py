# todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_and_create, name='task_list_and_create'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('remove/<int:pk>/', views.remove_task, name='remove_task'),
]
