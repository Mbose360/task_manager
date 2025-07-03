from django.urls import path
from .views import Registerview ,TaskListCreatView,TaskDetailView

urlpatterns = [
    path('register/',Registerview.as_view(),name='register'),
    path('tasks/', TaskListCreatView.as_view(),name='task_list_create'),
    path('tasks/<int:pk>',TaskDetailView.as_view(),name='task_detail'),
]
