from django.urls import path
from . import views

urlpatterns = [
    path("plecak/", views.backpack_view, name="backpack"),
    path("equip/<int:item_id>/", views.equip_item, name="equip_item"),
    path("unequip/<int:item_id>/", views.unequip_item, name="unequip_item"),
    path("give/<int:item_id>/", views.give_item, name="give_item"),
]
