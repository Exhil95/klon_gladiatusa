from django.urls import path
from . import views

urlpatterns = [
    path('profil/', views.WidokProfilu.as_view(), name='profil'),
    path('profil/rozdaj/', views.WidokRozdaniaStaystyk.as_view(), name='rozdaj_statystyki'),
    
]