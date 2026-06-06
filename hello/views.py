from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm




def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accout was created for ' + user )

            return redirect('LoginPage')

    context = {'form': form}
    return render(request, 'hello/register.html', context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Incorrect username or password')
    
        
    context = {}
    return render(request, 'hello/login2.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def signup(request):
    return render(request, 'hello/signup.html')

 
@login_required(login_url='login')
def home(request):
    return render(request, 'hello/home.html')
def about(request):
    return render(request, 'hello/about.html')
def editProfile(request):
    return render(request, 'hello/EditProfile.html')
def ac(request):
    return render(request, 'hello/ac.html')
def ae(request):
    return render(request, 'hello/ae.html')
def mv(request):
    return render(request, 'hello/mv.html')
