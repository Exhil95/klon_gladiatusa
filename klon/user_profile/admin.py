from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Widok dla strony admina.
    """
    list_display = ("user", "level", "experience", "stamina", "max_stamina", "strength", "dexterity", "constitution", "intelligence", "stat_points", "max_hp", "hp", "defence", "attack", "gold", "base_hp", "base_defence", "base_attack")
    list_filter = ("level",)
    search_fields = ("user__username",)
    ordering = ("-level",)
    fields = list_display
    list_editable = list_display[1:] 
    list_display_links = ("user",)  

class UserProfileInline(admin.StackedInline):
    """
    Opis administratora inline dla modelu UserProfile.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profil Gracza"

class CustomUserAdmin(UserAdmin):
    """
    Niestandardowy widok administratora dla modelu User z wbudowanym profilem użytkownika.
    """
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)