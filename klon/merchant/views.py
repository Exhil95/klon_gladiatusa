from django.shortcuts import render
from .models import Merchant

import random

def merchant_list(request):
    merchant = Merchant.objects.first()
    items = list(merchant.items.all())
    random_items = random.sample(items, min(len(items), 5))  # np. 5 losowych przedmiotów
    return render(request, 'merchant/merchant_list.html', {
        'merchant': merchant,
        'random_items': random_items
    })