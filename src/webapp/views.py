from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Tasks, choices_list
from webapp.forms import TaskForm

def index_view(request, *args, **kwargs):
    tasks = Tasks.objects.all()

    return render(request, 'index.html', context={
        'tasks': tasks
    })


def single_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    return render(request, 'single.html', context={
        'task': task
    })


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', context={'form':form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Tasks.objects.create(
                descr=form.cleaned_data['descr'],
                status=form.cleaned_data['status'],
                full_description=form.cleaned_data['full_description'],
                completion_date=form.cleaned_data['completion_date'])
            return redirect('task', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')


def task_update_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    print(task)
    if request.method == 'GET':
        form = TaskForm(data={
            'descr': task.descr,
            'status': task.status,
            'completion_date': task.completion_date,
            'full_description': task.full_description
        })
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.descr = form.cleaned_data['descr']
            task.status = form.cleaned_data['status']
            task.completion_date = form.cleaned_data['completion_date']
            task.full_description = form.cleaned_data['full_description']
            task.save()
            return redirect('task', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})