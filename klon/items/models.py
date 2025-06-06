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
        ('none', 'Brak'),  # dla mikstur itp.
    ]

    ITEM_TYPE_CHOICES = [
        ('equipment', 'Ekwipunek'),
        ('potion_hp', 'Mikstura HP'),
        ('potion_stamina', 'Mikstura Staminy'),
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
        help_text="Rzadkość przedmiotu"
    )
    slot = models.CharField(
        max_length=50,
        choices=SLOT_CHOICES,
        default='none',
        help_text="Slot, do którego pasuje przedmiot"
    )
    item_type = models.CharField(
        max_length=20,
        choices=ITEM_TYPE_CHOICES,
        default='equipment',
        help_text="Typ przedmiotu"
    )

    item_level = models.IntegerField(help_text="Poziom przedmiotu (ilvl)")
    dmg = models.IntegerField(default=0, help_text="Obrażenia przedmiotu")
    dmg_max = models.IntegerField(default=0, help_text="Maksymalne obrażenia przedmiotu")
    dmg_min = models.IntegerField(default=0, help_text="Minimalne obrażenia przedmiotu")
    item_strength = models.IntegerField(default=0, help_text="Siła przedmiotu")
    item_dexterity = models.IntegerField(default=0, help_text="Zręczność przedmiotu")
    item_constitution = models.IntegerField(default=0, help_text="Wytrzymałość przedmiotu")
    item_intelligence = models.IntegerField(default=0, help_text="Inteligencja przedmiotu")
    value = models.IntegerField(default=0, help_text="Wartość przedmiotu")
    
    effect_value = models.IntegerField(null=True, blank=True, help_text="Wartość efektu (np. HP +50)")

    def dmg_calc(self):
        self.dmg_max = self.dmg * 1.2
        self.dmg_min = self.dmg * 0.8
        self.save()

    def __str__(self):
        return self.name
