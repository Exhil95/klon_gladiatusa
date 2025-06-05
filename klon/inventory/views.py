from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryItem
from items.models import Item
from django.urls import reverse

@login_required
def backpack_view(request):
    all_items = InventoryItem.objects.all()
    my_items = InventoryItem.objects.filter(user=request.user)
    print("Zalogowany jako:", request.user.username)
    print("Moje przedmioty:", list(my_items))
    print("Wszystkie przedmioty:", list(all_items))
    return render(request, "inventory/backpackComponent.html", {"items": my_items})

@login_required
def equip_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    InventoryItem.objects.filter(user=request.user, item__slot=item.item.slot).update(equipped=False)
    item.equipped = True
    item.save()
    return redirect("profil")

@login_required
def unequip_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    item.equipped = False
    item.save()
    return redirect("profil")

@login_required
def give_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    InventoryItem.objects.create(user=request.user, item=item)
    return redirect("backpack")
