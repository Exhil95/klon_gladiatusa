from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from klon.inventory.models import Item

def backpack_view(request):
    items = Item.objects.all()
    return render(request, "inventory/backpackComponent.html", {"items": items})

def equip_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Item.objects.filter(type=item.type).update(equipped=False)
    item.equipped = True
    item.save()
    return redirect("backpack")

def unequip_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.equipped = False
    item.save()
    return redirect("backpack")
