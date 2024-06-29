from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Task
from .forms import TaskForm, CreateTask
# Create your views here.

def home(request):
    return render(request, 'index.html')


def dashboard(request):
    pass
    return render(request, 'dashboard.html')

def calendar(request):
    pass
    return render(request, 'calendar.html')

def quotes(request):
    pass
    return render(request, 'quotes.html')

#delete
def register(request): #rendering registration page
    return render(request, 'register.html')

def login(request): #rendering login page
    return render(request, 'login.html')





#create
def createTask(request): #rendering create task page
    form = CreateTask()
    #back end validation to check if its a post request
    if request.method == 'POST':
        form = CreateTask(request.POST)

        if form.is_valid():
            form.save() #sends data to database
            return redirect('view-tasks') #once task is created, user is sent back to dashboard

    context = {'form':form}
    return render(request, 'create-task.html', context=context)

#view (read)
def viewTask(request): #rendering view task page
    tasks = Task.objects.all()

    context = {'tasks':tasks}
    return render(request, 'view-tasks.html', context=context)

#update
def updateTask(request, pk): #rendering update task page, pk stands for primary key
    task = Task.objects.get(id=pk) #getting primary key (id) of task chosen
    form = TaskForm(instance=task) #edits specific task

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) #update task

        if form.is_valid(): #checking if form is valid
            form.save() #save updates

            return redirect('view-tasks') #redirects back to view tasks page

    context = {'form':form}
    return render(request, 'update-task.html', context=context)

#delete
def deleteTask(request, pk): #rendering delete task page
    task = Task.objects.get(id=pk) #getting primary key (id) of task chosen

    if request.method == 'POST':
        task.delete() #delete task

        return redirect('view-tasks') #redirects back to view tasks page

    context = {'object':task}
    return render(request, 'delete-task.html', context=context)

#calendar 
def calendar_events(request):
    all_tasks = Task.objects.all()
    out = []

    for task in all_tasks:
        out.append({
            'title': task.title,
            'start': task.date_due.strftime("%m/%d/%Y, %H:%M:%S")
        })


    return JsonResponse(out, safe=False)