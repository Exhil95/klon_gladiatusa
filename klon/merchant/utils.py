import random
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Item, MerchantOffer

RARITY_CONFIG = {
    'common':  {'count': 3, 'price_mult': 1.10},
    'uncommon': {'count': 2, 'price_mult': 1.50},
    'rare':    {'count': 1, 'price_mult': 2.00},
    'epic':    {'count': 1, 'price_mult': 5.00, 'chance': 0.05},
}

def generate_blacksmith_offer():
    MerchantOffer.objects.filter(type='blacksmith').delete()
    
    for rarity, config in RARITY_CONFIG.items():
        if rarity == 'epic' and random.random() > config['chance']:
            continue
        
        items = list(Item.objects.filter(rarity=rarity))
        selected = random.sample(items, min(config['count'], len(items)))
        
        for item in selected:
            MerchantOffer.objects.create(
                item=item,
                price=int(item.value * config['price_mult']),
                available_until=timezone.now() + timedelta(minutes=15),
                type='blacksmith'
            )
