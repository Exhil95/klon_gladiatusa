from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import RozdielPktStatystyk


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
            context.update({
                "player": player,
                "form": RozdielPktStatystyk(instance=player) if player.stat_points > 0 else None
            })
        return context

class WidokRozdaniaStaystyk(BazaWidokuProfilu, FormView):
    form_class = RozdielPktStatystyk
    template_name = "profil_gracza/profil.html" 

    def form_valid(self, form):
        player = self.get_user_profile()
        if isinstance(player, UserProfile):
            allocated_points = sum(filter(None, form.cleaned_data.values()))
            if allocated_points <= player.stat_points:
                player.stat_points -= allocated_points
                for field, value in form.cleaned_data.items():
                    if value:
                        setattr(player, field, getattr(player, field) + value)
                player.save()
                messages.success(self.request, "Punkty statystyk zostały rozdane!")
            else:
                messages.error(self.request, "Nie masz wystarczającej liczby punktów!")
        return redirect("profil")
