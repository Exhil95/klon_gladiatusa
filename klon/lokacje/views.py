from django.shortcuts import render
from .models import Location, Enemy
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required

def mapa_view(request):
    location = Location.objects.get(id=1)
    location2 = Location.objects.get(id=2)
    location3 = Location.objects.get(id=3)
    location4 = Location.objects.get(id=4)
    context = {
        'location': location,
        'location2': location2,
        'location3': location3,
        'location4': location4,
    }
    return render(request, 'lokacje/mapa.html', context)

def beast_dung_view(request):
    location = Location.objects.get(id = 1)
    enemies = location.enemies.all()
    return render(request, 'lokacje/beast_dung.html', {'location': location, 'enemies': enemies}) 

def circus_view(request):
    location = Location.objects.get(id = 2)
    enemies = location.enemies.all()
    return render(request, 'lokacje/circus.html', {'location': location, 'enemies': enemies}) 

def dessert_hills_view(request):
    location = Location.objects.get(id = 3)
    enemies = location.enemies.all()
    return render(request, 'lokacje/dessert_hills.html', {'location': location, 'enemies': enemies}) 

def plains_view(request):
    location = Location.objects.get(id = 4)
    enemies = location.enemies.all()
    return render(request, 'lokacje/plains.html', {'location': location, 'enemies': enemies})

@login_required
def fight_view(request, enemy_id):
    enemy = Enemy.objects.get(id=enemy_id)
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None  # lub obsłuż błąd w inny sposób
    
    context = {
        'enemy': enemy,
        'user_profile': user_profile,
    }
    return render(request, 'lokacje/fight.html', context)