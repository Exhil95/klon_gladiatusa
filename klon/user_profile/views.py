from django.shortcuts import render

def profil_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        sila = request.user.userprofile.strength
        zrecznosc = request.user.userprofile.dexterity
        budowa_fizyczna = request.user.userprofile.constitution
        inteligencja = request.user.userprofile.intelligence
    else:
        username = 'Nie jesteś zalogowany'
    return render(request, 'profil_gracza/profil.html', {
        'username': username, 
        'sila': sila, 
        'zrecznosc': zrecznosc, 
        'budowa_fizyczna': budowa_fizyczna, 
        'inteligencja': inteligencja
        })