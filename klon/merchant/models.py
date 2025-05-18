from django.db import models

# Create your models here.

class Merchant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.name} ({self.price} gold)"
    
    