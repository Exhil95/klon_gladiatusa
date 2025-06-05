from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapa_view, name='mapa'),
    path('circus/', views.circus_view, name='circus'),
    path('beast_dungeon/', views.beast_dung_view, name='beast_dung'),
    path('dessert_hills/', views.dessert_hills_view, name='dessert_hills'),
    path('plains/', views.plains_view, name='plains'),
    path('fight/<int:enemy_id>/', views.fight_view, name='fight'),
    path("ajax/refresh-banner/", views.refresh_banner, name="refresh_banner"),
]