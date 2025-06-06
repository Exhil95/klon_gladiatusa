from django.utils import timezone
from django.shortcuts import render
from .models import MerchantOffer
from .utils import generate_blacksmith_offer
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from inventory.models import InventoryItem
from .models import MerchantOffer
from django.shortcuts import get_object_or_404
from user_profile.models import UserProfile
from django.views.decorators.http import require_POST


@login_required
def blacksmith_page_view(request):
    offers = MerchantOffer.objects.filter(type='blacksmith', available_until__gte=timezone.now())
    backpack = InventoryItem.objects.filter(user=request.user)

    for item in backpack:
        item.sell_price = int(item.item.value * 0.8)

    return render(request, "merchants/blacksmith.html", {
        "offers": offers,
        "backpack": backpack,
    })

@login_required
def blacksmith_offer_fragment(request):
    offers = MerchantOffer.objects.filter(type='blacksmith', available_until__gte=timezone.now())
    return render(request, 'merchants/partials/blacksmith_offer.html', {'offers': offers})


def merchant_view(request):
    return render(request, 'merchants/merchant.html', {
        'blacksmith_offers': MerchantOffer.objects.filter(type='blacksmith', available_until__gte=timezone.now()),
        #'alchemist_offers': MerchantOffer.objects.filter(type='alchemist', available_until__gte=timezone.now())
    })
    
@login_required
def buy_offer_view(request, offer_id):
    offer = get_object_or_404(MerchantOffer, id=offer_id)
    player = UserProfile.objects.get(user=request.user)  

    if offer.available_until < timezone.now():
        return JsonResponse({'error': 'Oferta wygasła.'}, status=400)

    if player.gold < offer.price:
        return JsonResponse({'error': 'Za mało złota.'}, status=400)

    # Odjęcie złota
    player.gold -= offer.price
    player.save()

    # Dodanie itemu do inventory
    InventoryItem.objects.create(user=request.user, item=offer.item)

    return JsonResponse({
        'success': f'Kupiono {offer.item.name} za {offer.price} złota.',
        'gold': player.gold
    })
    
@login_required
@require_POST
def sell_to_merchant(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id, user=request.user)
    user_profile = UserProfile.objects.get(user=request.user)

    value = int(item.item.value * 0.8)
    user_profile.gold += value
    user_profile.save()
    item.delete()

    return HttpResponse("")

@login_required
def backpack_fragment(request):
    backpack = InventoryItem.objects.filter(user=request.user)

    for item in backpack:
        item.sell_price = int(item.item.value * 0.8)

    return render(request, "merchants/backpack_partial.html", {"backpack": backpack})
