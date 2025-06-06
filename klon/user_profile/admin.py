from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user", "level", "experience", "stat_points", "gold",
        "hp", "max_hp", "stamina", "max_stamina",
        "attack", "defence"
    )
    list_filter = ("level",)
    search_fields = ("user__username",)
    ordering = ("-level",)
    list_display_links = ("user",)
    readonly_fields = (
         "last_regen", "last_regen_stm"
    )

    fieldsets = (
        ("Gracz", {
            "fields": ("user", "level", "experience", "stat_points", "gold")
        }),
        ("Statystyki główne", {
            "fields": ("strength", "dexterity", "constitution", "intelligence")
        }),
        ("Punkty życia i stamina", {
            "fields": ("hp", "max_hp", "stamina", "max_stamina", "last_regen", "last_regen_stm")
        }),
        ("Statystyki walki", {
            "fields": ("attack", "defence", )
        }),
        ("Bazowe statystyki", {
            "fields": (
                "base_hp", "base_attack", "base_defence",
                "base_strength", "base_dexterity", "base_constitution", "base_intelligence"
            )
        }),
    )
