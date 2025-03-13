from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Tworzenie instancji UserProfile przy rejestracji gracza.
    """
    if created:  
        UserProfile.objects.create(user=instance)
        print(f"Utworzono profil dla {instance.username}")