from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    files = myfiles.objects.filter(user=request.user)
    context = {'files':files}
    return render(request, 'index.html', context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def signupUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.save()
        messages.success(request, "Account Created successfully !")
    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def upload(request):
    if request.method == "POST":
        files = request.FILES.getlist("choosefiles")
        user = (request.POST.get('user'))
        for file in files:
            record = myfiles(file=file, user=user)
            record.save()
        return redirect('index')

def delete(request, pk):
    if request.method == "POST":
        file = myfiles.objects.get(pk=pk)
        file.delete()
        return redirect('index')

def del_user(request):
    u = User.objects.get(username = request.user)
    userfiles = myfiles.objects.filter(user = request.user)
    for file in userfiles:
        file.delete()
    u.delete()
    messages.success(request, "The Account Deleted !")
    return render(request, 'login.html')