from django.db import models
from django.utils import timezone
from items.models import Item

class MerchantOffer(models.Model):
    MERCHANT_TYPES = [
        ('blacksmith', 'Kowal'),
        ('alchemist', 'Alchemik'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    available_until = models.DateTimeField()
    type = models.CharField(max_length=20, choices=MERCHANT_TYPES)

    def is_active(self):
        return self.available_until >= timezone.now()

    def __str__(self):
        return f"{self.get_type_display()} oferuje {self.item.name} za {self.price}"
