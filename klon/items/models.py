from django.db import models

class Item(models.Model):
    SLOT_CHOICES = [
        ('head', 'Head'),
        ('chest', 'Chest'),
        ('legs', 'Legs'),
        ('feet', 'Feet'),
        ('hands', 'Hands'),
        ('weapon', 'Weapons'),
        ('shield', 'Shield'),
        ('accessory', 'Accessory'),
    ]

    name = models.CharField(max_length=100, unique=True, help_text="Nazwa przedmiotu")
    description = models.TextField(blank=True, help_text="Opis przedmiotu")
    rarity = models.CharField(
        max_length=50,
        choices=[
            ('common', 'Common'),
            ('uncommon', 'Uncommon'),
            ('rare', 'Rare'),
            ('epic', 'Epic'),
            ('legendary', 'Legendary'),
        ],
        default='common',
        help_text= "Rzadkość przedmiotu"
    )
    slot = models.CharField(
        max_length=50,
        choices=SLOT_CHOICES,
        help_text="Slot, do którego pasuje przedmiot"
    )
    item_level = models.IntegerField(help_text="Poziom przedmiotu(ilvl)")
    drop_chance = models.FloatField(help_text="Szansa na drop w procentach")
    value = models.IntegerField(default=0, help_text="Wartość przedmiotu")

    def __str__(self):
        return self.name
    

