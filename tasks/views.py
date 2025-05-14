from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def task_list(request):
    query = request.GET.get('q', '')
    filter_option = request.GET.get('filter', 'all')

    tasks = Task.objects.filter(user=request.user)

    if filter_option == 'completed':
        tasks = tasks.filter(complete=True)
    elif filter_option == 'pending':
        tasks = tasks.filter(complete=False)

    if query:
        tasks = tasks.filter(Q(title__icontains=query))

    tasks = tasks.order_by('-created')
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks/task_list.html', {
        'tasks': page_obj,
        'query': query,
        'filter_option': filter_option,
        'page_obj': page_obj,
    })


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect('task_list')

