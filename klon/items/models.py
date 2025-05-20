from django.db import models

class Item(models.Model):
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
    drop_chance = models.FloatField(help_text="Szansa na drop w procentach")
    value = models.IntegerField(default=0, help_text="Wartość przedmiotu")

    def __str__(self):
        return self.name
