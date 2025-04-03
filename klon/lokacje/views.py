from django.shortcuts import render
from .models import Location, Enemy

def mapa_view(request):
    location = Location.objects.get(id=1)
    location2 = Location.objects.get(id=2)
    print(location)
    return render(request, 'lokacje/mapa.html', {'location': location, 'location2': location2})

def beast_dung_view(request):
    location = Location.objects.get(name="Zdziczałe Lochy")
    enemies = location.enemies.all()
    return render(request, 'lokacje/beast_dung.html', {'location': location, 'enemies': enemies}) 

def circus_view(request):
    return render(request, 'lokacje/circus.html', {}) 

def dessert_hills_view(request):
    return render(request, 'lokacje/dessert_hills.html', {}) 

def plains_view(request):
    return render(request, 'lokacje/plains.html', {}) 
