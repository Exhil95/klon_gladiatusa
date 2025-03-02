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
            messages.success(request, ("Błąd przy logowaniu, spróbuj ponownie"))
            return redirect('login_user')
            pass
    
    
    else:
        return render(request, 'authenticate/login.html', {})
    

