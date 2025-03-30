from django.shortcuts import render

def mapa_view(request):
    return render(request, 'lokacje/mapa.html', {})

def beast_dung_view(request):
    return render(request, 'lokacje/beast_dung.html', {}) 

def circus_view(request):
    return render(request, 'lokacje/circus.html', {}) 

def dessert_hills_view(request):
    return render(request, 'lokacje/dessert_hills.html', {}) 

def plains_view(request):
    return render(request, 'lokacje/plains.html', {}) 
