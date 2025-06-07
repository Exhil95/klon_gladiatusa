from django.db import models
from django.contrib.auth.models import User
from klon.items.models import Item

class InventoryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    equipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item.name} ({self.user.username}){' [Equipped]' if self.equipped else ''}"
