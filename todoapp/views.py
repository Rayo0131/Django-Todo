from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm, CustomUserCreationForm


from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request, "index.html")

def About(request):
    return render(request, "about.html")

def Services(request):
    return render(request, "services.html")


def Contact(request):
    return render(request, "contact.html")

def Signup(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect('task_list')

    # else:
    #     form = UserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


    return render(request, "registration/signup.html", {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)


    return render(request, "task_list.html", {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task =form.save(commit = False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()        

    
    return render(request, "task_create.html", {'form': form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user) 
    task.delete()
    return redirect('task_list')
