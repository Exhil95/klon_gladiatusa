from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    equipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.type}){' [Equipped]' if self.equipped else ''}"