from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
