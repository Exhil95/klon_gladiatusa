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
            return redirect('profil')
        else:
            messages.success(request, ("Błąd przy logowaniu, spróbuj ponownie"))
            return redirect('login_user')
            pass
    
    
    else:
        return render(request, 'authenticate/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Wylogowano"))
    return redirect('login_user')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Zarejestrowano"))
            return redirect('profil')
    else:
        form = UserCreationForm()
    
    return render(request, 'authenticate/register.html', {'form': form})