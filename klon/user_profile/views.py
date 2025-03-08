from django.shortcuts import render

def profil_view(request):
    return render(request, 'profil_gracza/profil.html', {})
