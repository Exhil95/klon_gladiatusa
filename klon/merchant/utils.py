from django.utils import timezone
from datetime import timedelta
from .models import MerchantOffer
from items.models import Item
import random

def generate_blacksmith_offer():
    now = timezone.now()

    # Jeśli nie trzeba jeszcze odświeżać, pomiń
    next_refresh_time = now.replace(minute=(now.minute // 15) * 15) + timedelta(minutes=15)
    if MerchantOffer.objects.filter(type='blacksmith', available_until__gte=now).exists():
        return

    # Usuń starą ofertę
    MerchantOffer.objects.filter(type='blacksmith').delete()

    # Dodaj nową
    for _ in range(5):
        item = random.choice(Item.objects.all())
        MerchantOffer.objects.create(
            item=item,
            type='blacksmith',
            price=item.value,
            available_until=next_refresh_time,
            stock=random.randint(1, 3)
        )


def generate_alchemist_offer():
    from items.models import Item
    from .models import MerchantOffer
    from django.utils import timezone
    from datetime import timedelta
    import random

    now = timezone.now()
    next_refresh = now.replace(minute=(now.minute // 15) * 15) + timedelta(minutes=15)

    # Jeśli już jest aktywna oferta, nie generuj ponownie
    if MerchantOffer.objects.filter(type='alchemist', available_until__gte=now).exists():
        return

    # Usuń stare oferty alchemika
    MerchantOffer.objects.filter(type='alchemist').delete()

    # Pobierz tylko mikstury
    potion_items = Item.objects.filter(item_type__in=['potion_hp', 'potion_stamina'])

    for item in random.sample(list(potion_items), k=min(5, len(potion_items))):
        MerchantOffer.objects.create(
            item=item,
            type='alchemist',
            price=item.value,
            available_until=next_refresh,
            stock=random.randint(1, 5)
        )
