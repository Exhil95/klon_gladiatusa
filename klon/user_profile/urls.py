from django.urls import path
from . import views
from .views import WidokProfilu, profil_gracza

urlpatterns = [
    path('profil/', views.WidokProfilu.as_view(), name='profil'),
    path('profil/rozdaj/', views.WidokRozdaniaStaystyk.as_view(), name='rozdaj_statystyki'),
    path('profil/', profil_gracza, name='profil'),
]