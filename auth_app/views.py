from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})
    
    
def view_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User's Name or Password inccorect.")
    return render(request, 'sign_in.html')

@login_required
def view_home(request):
    return render(request, 'home.html')

def view_logout(request):
    logout(request)
    return redirect('signin')