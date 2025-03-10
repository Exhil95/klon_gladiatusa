from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile


class BazaWidokuProfilu(LoginRequiredMixin, View):

    def get_user_profile(self):
        try:
            return self.request.user.userprofile
        except UserProfile.DoesNotExist:
            messages.error(self.request, "Nie znaleziono profilu gracza. Zarejestruj lub zaloguj.")
            return redirect("login_user")  


class WidokProfilu(BazaWidokuProfilu, TemplateView):
    template_name = "profil_gracza/profil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.get_user_profile()
        if isinstance(player, UserProfile):
            player.dodaj_exp(0)  
            experience_percentage = round((player.experience / player.lvlup_exp()) * 100)
            print(f"Dostępne pkt stystyk: {player.stat_points}")
            print(f"Procent doświadczenia: {experience_percentage}%")
            context.update({
                "player": player,
                "experience_percentage": experience_percentage,
            })
        return context

class WidokRozdaniaStaystyk(BazaWidokuProfilu, View):

    def get(self, request, *args, **kwargs):
        player = self.get_user_profile()
        stat = request.GET.get('stat')
        if stat and player.stat_points > 0:
            if hasattr(player, stat):
                setattr(player, stat, getattr(player, stat) + 1)
                player.stat_points -= 1
                player.save()
                messages.success(request, f"Punkt dodany do {stat}!")
            else:
                messages.error(request, "Nieprawidłowa statystyka!")
        else:
            messages.error(request, "Nie masz wystarczającej liczby punktów!")
        return redirect("profil")
