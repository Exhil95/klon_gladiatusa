from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryItem
from items.models import Item
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from user_profile.models import UserProfile
from django.template.loader import render_to_string



@login_required
def backpack_view(request):
    all_items = InventoryItem.objects.all()
    my_items = InventoryItem.objects.filter(user=request.user)
    return render(request, "inventory/backpackComponent.html", {"items": my_items})

@login_required
def equip_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    InventoryItem.objects.filter(user=request.user, item__slot=item.item.slot).update(equipped=False)
    item.equipped = True
    item.save()
    request.user.userprofile.update_stats()
    return redirect("profil")

@login_required
def unequip_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    item.equipped = False
    item.save()
    request.user.userprofile.update_stats()
    return redirect("profil")

@login_required
def give_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    InventoryItem.objects.create(user=request.user, item=item)
    return redirect("backpack")


@login_required
@require_POST
def use_potion(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    player = UserProfile.objects.get(user=request.user)

    if item.item.item_type == 'potion_hp':
        player.hp = min(player.max_hp, player.hp + item.item.effect_value)
    elif item.item.item_type == 'potion_stamina':
        player.stamina = min(player.max_stamina, player.stamina + item.item.effect_value)
    else:
        return JsonResponse({'error': 'To nie jest mikstura'}, status=400)

    player.save()
    item.delete()
    return JsonResponse({'success': 'Użyto mikstury'})

@login_required
def refresh_banner(request):
    try:
        player = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return HttpResponse("")
    return HttpResponse(
        render_to_string("banner_up.html", {"player": player}, request=request)
    )