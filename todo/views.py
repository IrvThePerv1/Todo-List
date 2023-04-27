from django.shortcuts import render,redirect
from .models import TodoL
from .form import CreateTask
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('list')
    
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not excist')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            messages.error(request,"Username or Password are incorrect")
    return render(request,'todo/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {"form":form}
    return render(request,'todo/register.html',context)


@login_required(login_url='login')
def list(request):
    tasks = TodoL.objects.filter(user=request.user)
    context={"tasks":tasks}
    return render(request,'todo/home.html',context)

def item(request,pk):
    task = TodoL.objects.get(id=pk)
    context = {"task":task}
    return render(request,'todo/item.html',context)


@login_required()
def createTask(request):
    form = CreateTask()
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list')
    context = {"form": form}
    return render(request, 'todo/create-task.html', context)

@login_required()
def updateTask(request,pk):
    task = TodoL.objects.get(id=pk)
    form = CreateTask(instance=task)

    if request.method == "POST":
        form = CreateTask(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {"form":form}
    return render(request,'todo/create-task.html',context)

@login_required()
def deleteTask(request,pk):
    task = TodoL.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('list')
    context = {"task":task}
    return render(request,'todo/delete.html',context)

