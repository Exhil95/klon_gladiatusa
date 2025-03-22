from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from django.http import HttpResponse


class BazaWidokuProfilu(LoginRequiredMixin, View):
    """
    Klasa bazowa dla widoków profilu gracza, w tym wypadku zastowanie CBV[Class Based Views], ze względu na bardziej rozbudowaną formę.
    Używa LoginRequiredMixin do sprawdzenia czy użytkownik jest zalogowany.
    Renderuje profil gracza.
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
        Oblicza procenty doświadczenia i zdrowia.
        """
        context = super().get_context_data(**kwargs)
        player = self.get_user_profile()
        if isinstance(player, UserProfile):
            player.dodaj_exp(0)
            player.hp_regen()  
            experience_percentage = round((player.experience / player.lvlup_exp()) * 100)
            hp_percentage = round((player.hp / player.max_hp) * 100)
            print(f"Procent zdrowia: {hp_percentage}%")
            print(f"Dostępne pkt stystyk: {player.stat_points}")
            print(f"Procent doświadczenia: {experience_percentage}%")
            context.update({
                "player": player,
                "experience_percentage": experience_percentage,
                "hp_percentage": hp_percentage, 
            })
        return context

class WidokRozdaniaStaystyk(BazaWidokuProfilu, View):
    """
    Widok rozdania punktów statystyk
    """

    def get(self, request, *args, **kwargs):
        """
        Obsługa GET requestu.
        oblicza statystyki gracza.
        """
        player = self.get_user_profile()
        stat = request.GET.get('stat')
        if stat and player.stat_points > 0:
            if hasattr(player, stat):
                setattr(player, stat, getattr(player, stat) + 1)
                player.stat_points -= 1
                player.base_hp = 100 + player.constitution * 25
                player.base_defence = player.constitution + player.dexterity # ratio do zmiany balansu
                player.base_attack = player.strength + player.intelligence # ratio do zmiany balansu
                player.attack = player.base_attack # + item_attack dodane w przyszłości 
                player.defence = player.base_defence # + item_defence dodane w przyszłości
                player.max_hp = player.base_hp # + item_hp dodane w przyszłości
                #item attack, defence, hp trzeba rozwiązać skalowanie dodawanie itp
                player.save()
                messages.success(request, f"Punkt dodany do {stat}!")
            else:
                messages.error(request, "Nieprawidłowa statystyka!")
        else:
            messages.error(request, "Nie masz wystarczającej liczby punktów!")
        return redirect("profil")

