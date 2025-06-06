from django.db import models
from django.core.exceptions import ValidationError
from items.models import Item

class Enemy(models.Model):
    """
    Model wroga
    """
    ENEMY_TYPES = [
        ('normal', 'Normalny'),
        ('elite', 'Elita'),
        ('boss', 'Boss'),
    ]

    name = models.CharField(max_length=25, default="test_object")
    description = models.TextField(default="Opis przeciwnika", blank=True)
    lvl = models.PositiveIntegerField(default=1)
    base_strenght = models.IntegerField(default=1)  
    base_intelect = models.IntegerField(default=1)  
    base_dexterity = models.IntegerField(default=1)
    base_constitution = models.IntegerField(default=1)
    gold_drop = models.IntegerField(default=0)
    base_hp = models.IntegerField(default=100)
    base_attack = models.IntegerField(default=0)
    base_defence = models.IntegerField(default=0)
    loot_table = models.ManyToManyField(Item, blank=True, related_name='loot_table')
    type = models.CharField(max_length=10, choices=ENEMY_TYPES, default='normal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    drop_chance = models.DecimalField(decimal_places=2, max_digits=3, default=0.01)
    portrait = models.ImageField(upload_to="portraits/", blank=True, null=True, help_text="Portret wroga") 

    def __str__(self):
        """Zwraca nazwę wroga w postaci stringa"""
        return self.name

    def calculate_stats(self):
        """
        Kalkuluje statystyki na podstawie poziomu i bazowych statystyk.
        """
        self.base_hp = 100 + self.lvl * 20
        self.base_attack = self.base_strenght * 2 + self.lvl
        self.base_defence = self.base_dexterity * 2 + self.lvl

    def clean(self):
        """
        Waliduje poziom i zwraca błąd.
        """
        if self.lvl < 1:
            raise ValidationError("Poziom przeciwnika nie może być mniejszy niż 1.")

class Location(models.Model):
    """
    Model lokacji, pobiera dane relacją ManyToMany z wroga.
    """
    name = models.CharField(max_length=25, default="test_location")
    enemies = models.ManyToManyField('Enemy', related_name='locations')

    def __str__(self):
        """Zwraca nazwę lokacji."""
        return self.name

