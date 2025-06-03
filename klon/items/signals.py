from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item



#@receiver(post_save, sender=Item)
#def calculate_dmg(sender, instance, created, **kwargs):
#    """
#    Kalkulacja DMG.
#    """
#    if created:  
#        Item.dmg_calc(instance)
#        instance.save()
#        print(f"skalkulowano DMG dla {instance.name}")