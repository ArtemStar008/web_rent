from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all
    return render(request,'main/index.html', {'tasks' : tasks})


def about(request):
    return render(request,'main/about.html')

def ok_order(request):
    return render(request,'main/ok_order.html')

def made(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ok_order')
        else:
            error = 'неверно'

    form = TaskForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request,'main/made.html', context)