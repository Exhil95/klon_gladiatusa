from django.shortcuts import render
from .models import Merchant
from django.contrib.auth.decorators import login_required
import random


@login_required
def merchant_list(request):
    merchant = Merchant.objects.first()
    items = list(merchant.inventory.all())
    random_items = random.sample(items, min(len(items), 5))  # np. 5 losowych przedmiotów
    context = {
        'merchant': merchant,
        'random_items': random_items
    }
    return render(request, 'merchant/merchant_list.html', context)