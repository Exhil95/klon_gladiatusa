from django.db import models
from items import Item

class InventoryItem(models.Model): #do przerobienia na spokojnie foreignkeyem
    name = models.CharField(max_length=100)
    type = models.CharField(
        choices = [
        ('head', 'Head'),
        ('chest', 'Chest'),
        ('legs', 'Legs'),
        ('feet', 'Feet'),
        ('hands', 'Hands'),
        ('weapon', 'Weapons'),
        ('shield', 'Shield'),
        ('accessory', 'Accessory'),
    ],
        default="accessory"
    ) 
    equipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.type}){' [Equipped]' if self.equipped else ''}"