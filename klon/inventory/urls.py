from django.urls import path
from klon.items import views

urlpatterns = [
    path('backpack/', views.backpack_view, name='backpack'),
    path('equip/<int:item_id>/', views.equip_item, name='equip_item'),
    path('unequip/<int:item_id>/', views.unequip_item, name='unequip_item'),
]
