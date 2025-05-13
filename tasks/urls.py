from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
]
