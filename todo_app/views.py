from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def task_list_and_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list_and_create')
    else:
        form = TodoForm()

    tasks = Todo.objects.all()
    return render(request, 'todo_app/index.html', {'form': form, 'tasks': tasks})


def edit_task(request, pk):
    try:
        task = get_object_or_404(Todo, pk=pk)
        if request.method == 'POST':
            form = TodoForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list_and_create')
        else:
            form = TodoForm(instance=task)
        return render(request, 'todo_app/edit_task.html', {'form': form, 'task': task})
    except Exception as e:
        print("Error in editing task:", e)
        raise e

def remove_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list_and_create')
    return render(request, 'todo_app/remove_task.html', {'task': task})
