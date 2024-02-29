from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# Create your views here.

# @login_required(login_url="login-user")
def dashboard(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request,'profile/dashboard.html', context)

# create task

def create_task(request):
    form = TaskForm()
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    
    context = {'form': form,'tasks': tasks}
    return render(request,"profile/create_task.html",context)