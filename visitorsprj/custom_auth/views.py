from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from visitorsprj.settings import LOGIN_URL
from custom_auth.forms import RegisterForm, LoginForm

def index(request):
    return render(request, 'auth/index.html')

from django.shortcuts import render, redirect
from custom_auth.forms import RegisterForm  # Import your RegisterForm

def registerView(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', { 'form': form, 'msg': msg })



def loginView(request):
    msg = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('visitor')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', { 'form': form, 'msg': msg })


def logoutView(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return render(request, "auth/logout.html")
