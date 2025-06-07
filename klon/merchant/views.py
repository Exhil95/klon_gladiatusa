from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import MerchantOffer
from .utils import generate_blacksmith_offer, generate_alchemist_offer
from klon.inventory.models import InventoryItem
from klon.user_profile.models import UserProfile



# --- KOWAL ---

@login_required
def blacksmith_page_view(request):
    generate_blacksmith_offer()
    offers = MerchantOffer.objects.filter(
        type='blacksmith',
        available_until__gte=timezone.now(),
        stock__gt=0
    )
    backpack = InventoryItem.objects.filter(user=request.user)
    for item in backpack:
        item.sell_price = int(item.item.value * 0.8)
    return render(request, 'merchants/blacksmith.html', {
        'offers': offers,
        'backpack': backpack,
    })

@login_required
def blacksmith_offer_fragment(request):
    offers = MerchantOffer.objects.filter(
        type='blacksmith',
        available_until__gte=timezone.now(),
        stock__gt=0
    )
    return render(request, 'merchants/partials/blacksmith_offer.html', {'offers': offers})

@login_required
def buy_offer_view(request, offer_id):
    offer = get_object_or_404(MerchantOffer, id=offer_id)
    player = UserProfile.objects.get(user=request.user)

    if offer.available_until < timezone.now():
        return JsonResponse({'error': 'Oferta wygasła.'}, status=400)

    if offer.stock <= 0:
        return JsonResponse({'error': 'Brak dostępnych sztuk.'}, status=400)

    if player.gold < offer.price:
        return JsonResponse({'error': 'Za mało złota.'}, status=400)

    # Zmniejszenie zapasu i zapis
    offer.stock -= 1
    offer.save()

    # Dodanie itemu i odjęcie złota
    InventoryItem.objects.create(user=request.user, item=offer.item)
    player.gold -= offer.price
    player.save()

    return JsonResponse({
        'success': f'Kupiono {offer.item.name}.',
        'stock': offer.stock,
        'gold': player.gold
    })

@login_required
@require_POST
def sell_to_merchant(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    player = UserProfile.objects.get(user=request.user)
    value = int(item.item.value * 0.8)
    player.gold += value
    player.save()
    item.delete()
    return HttpResponse("")

@login_required
def backpack_fragment(request):
    backpack = InventoryItem.objects.filter(user=request.user)
    for item in backpack:
        item.sell_price = int(item.item.value * 0.8)
    return render(request, "merchants/backpack_partial.html", {"backpack": backpack})

# --- ALCHEMIST ---

@login_required
def alchemist_page_view(request):
    generate_alchemist_offer()
    offers = MerchantOffer.objects.filter(
        type='alchemist',
        available_until__gte=timezone.now(),
        stock__gt=0
    )
    backpack = InventoryItem.objects.filter(user=request.user)
    for item in backpack:
        item.sell_price = int(item.item.value * 0.8)
    return render(request, "merchants/alchemist.html", {
        "offers": offers,
        "backpack": backpack,
    })

@login_required
def backpack_fragment_alchemist(request):
    backpack = InventoryItem.objects.filter(user=request.user)
    for item in backpack:
        item.sell_price = int(item.item.value * 0.8)
    return render(request, "merchants/backpack_partial.html", {"backpack": backpack})

@login_required
@require_POST
def buy_offer_alchemist(request, offer_id):
    offer = get_object_or_404(MerchantOffer, id=offer_id, type='alchemist')
    player = UserProfile.objects.get(user=request.user)

    if offer.available_until < timezone.now():
        return JsonResponse({'error': 'Oferta wygasła.'}, status=400)
    if offer.stock <= 0:
        return JsonResponse({'error': 'Brak dostępnych sztuk.'}, status=400)
    if player.gold < offer.price:
        return JsonResponse({'error': 'Za mało złota.'}, status=400)

    offer.stock -= 1
    offer.save()
    player.gold -= offer.price
    player.save()
    InventoryItem.objects.create(user=request.user, item=offer.item)

    return JsonResponse({
        'success': f'Kupiono {offer.item.name}.',
        'stock': offer.stock,
        'gold': player.gold,
    })


@login_required
@require_POST
def sell_to_alchemist(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    player = UserProfile.objects.get(user=request.user)
    value = int(item.item.value * 0.8)
    player.gold += value
    player.save()
    item.delete()
    return HttpResponse("")

# --- OGÓLNY WIDOK HANDLARZA ---

def merchant_view(request):
    return render(request, 'merchants/merchant.html', {
        'blacksmith_offers': MerchantOffer.objects.filter(type='blacksmith', available_until__gte=timezone.now()),
        # 'alchemist_offers': MerchantOffer.objects.filter(type='alchemist', available_until__gte=timezone.now())
    })

