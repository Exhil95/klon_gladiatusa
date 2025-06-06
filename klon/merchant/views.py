from django.utils import timezone
from django.shortcuts import render
from .models import MerchantOffer
from .utils import generate_blacksmith_offer


def blacksmith_offer_view(request):
    generate_blacksmith_offer()  
    offers = MerchantOffer.objects.filter(type='blacksmith', available_until__gte=timezone.now())
    return render(request, 'merchants/partials/blacksmith_offer.html', {'offers': offers})


def merchant_view(request):
    return render(request, 'merchants/merchant.html', {
        'blacksmith_offers': MerchantOffer.objects.filter(type='blacksmith', available_until__gte=timezone.now()),
        #'alchemist_offers': MerchantOffer.objects.filter(type='alchemist', available_until__gte=timezone.now())
    })