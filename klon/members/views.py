from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_user')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
            pass
    
    
    else:
        return render(request, 'authenticate/login.html', {})
    

