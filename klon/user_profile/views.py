from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from klon.inventory.models import InventoryItem

class BazaWidokuProfilu(LoginRequiredMixin, View):
    """
    Klasa bazowa dla widoków profilu gracza.
    Używa LoginRequiredMixin do sprawdzenia czy użytkownik jest zalogowany.
    """

    def get_user_profile(self):
        try:
            return self.request.user.userprofile
        except UserProfile.DoesNotExist:
            messages.error(self.request, "Nie znaleziono profilu gracza. Zarejestruj lub zaloguj.")
            return redirect("login_user")

class WidokProfilu(BazaWidokuProfilu, TemplateView):
    """
    Widok profilu gracza.
    """
    template_name = "profil_gracza/profil.html"

    def get_context_data(self, **kwargs):
        """
        Wysyła dane gracza do szablonu profilu gracza.
        Oblicza procenty doświadczenia, zdrowia i staminy.
        """
        context = super().get_context_data(**kwargs)
        player = self.get_user_profile()
        if isinstance(player, UserProfile):
            # Regeneracja i aktualizacja expa
            player.dodaj_exp(0)
            player.hp_regen()
            player.stamina_regen()
            # Wyliczenia procentowe
            experience_percentage = round((player.experience / player.lvlup_exp()) * 100) if player.lvlup_exp() else 0
            hp_percentage = round((player.hp / player.max_hp) * 100) if player.max_hp else 0
            stamina_percentage = round((player.stamina / player.max_stamina) * 100) if player.max_stamina else 0

            context.update({
                "items": InventoryItem.objects.filter(user=player.user),
                "player": player,
                "experience_percentage": experience_percentage,
                "hp_percentage": hp_percentage,
                "stamina_percentage": stamina_percentage,
                "tooltips": {
                    "strength": "Siła wpływa na obrażenia zadawane przeciwnikom.",
                    "dexterity": "Zręczność zwiększa obronę.",
                    "constitution": "Budowa fizyczna zwiększa maksymalne punkty życia i wpływa na regenerację punktów życia.",
                    "intelligence": "Inteligencja wpływa na szybkość regeneracji punktów życia."
                }
            })
        return context

class WidokRozdaniaStaystyk(BazaWidokuProfilu, View):
    """
    Widok do rozdawania punktów statystyk.
    """
    def get(self, request, *args, **kwargs):
        player = self.get_user_profile()
        stat = request.GET.get("stat")

        if not stat or not isinstance(player, UserProfile) or player.stat_points <= 0:
            messages.error(request, "Nie masz wystarczającej liczby punktów!")
            return redirect("profil")

        base_fields = {
            "strength": "base_strength",
            "dexterity": "base_dexterity",
            "constitution": "base_constitution",
            "intelligence": "base_intelligence"
        }

        if stat in base_fields:
            field_name = base_fields[stat]
            setattr(player, field_name, getattr(player, field_name) + 1)
            player.stat_points -= 1

            # Aktualizacja statystyk
            player.base_hp = 100 + player.base_constitution * 25
            player.base_defence = player.base_constitution + player.base_dexterity
            player.base_attack = player.base_strength + player.base_intelligence
            player.update_stats()

            messages.success(request, f"Punkt dodany do {stat}!")
        else:
            messages.error(request, "Nieprawidłowa statystyka!")

        return redirect("profil")

def profil_gracza(request):
    """
    Widok funkcjonalny profilu gracza (opcjonalny, jeśli korzystasz z CBV).
    """
    tooltips = {
        "strength": "Siła wpływa na obrażenia zadawane przeciwnikom.",
        "dexterity": "Zręczność zwiększa obronę",
        "constitution": "Budowa fizyczna zwiększa maksymalne punkty życia i wpływa na regenerację punktów życia.",
        "intelligence": "Inteligencja wpływa na szybkość regeneracji punktów życia."
    }
    return render(request, 'profil_gracza/profil.html', {
        'player': request.user.userprofile,
        'tooltips': tooltips
    })