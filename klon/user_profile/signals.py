from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Tworzy instancję UserProfile przy rejestracji użytkownika,
    lub zapisuje istniejący profil przy aktualizacji User.
    """
    if created:
        UserProfile.objects.create(user=instance)
        print(f"Utworzono profil dla {instance.username}")
    else:
        # Zapewnia, że profil istnieje i jest aktualizowany przy każdej zmianie User
        UserProfile.objects.get_or_create(user=instance)