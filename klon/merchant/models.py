from django.db import models
from items.models import Item

# Create your models here.

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    inventory = models.ManyToManyField(Item, blank=True, help_text="Przedmioty dostępne u kupca", default=None)
    description = models.TextField(blank=True, help_text="Opis kupca", default="")

    def __str__(self):
        return self.name
    

    
    