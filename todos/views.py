from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# Create your views here.



@login_required(login_url="login-user")
def dashboard(request):
    current_user = request.user.id
    
    tasks = Task.objects.all().filter(owner=current_user)
    # tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request,'profile/dashboard.html', context)

# create task
@login_required(login_url="login-user")
def create_task(request):
    form = TaskForm()
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # connecting task with the owner of the task
            task.owner = request.user
            
            task.save()
            return redirect("dashboard")
    
    context = {'form': form,'tasks': tasks}
    return render(request,"profile/create_task.html",context)

@login_required(login_url="login-user")
def delete_task(request, id):
    task_done = Task.objects.get(id = id)
    task_done.delete()
   

    return redirect("dashboard")
    
    