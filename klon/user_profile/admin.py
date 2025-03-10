from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "level", "experience", "strength", "dexterity", "constitution", "intelligence", "stat_points")
    list_filter = ("level",)
    search_fields = ("user__username",)
    ordering = ("-level",)
    fields = ("user", "level", "experience", "stat_points", "strength", "dexterity", "constitution", "intelligence")
    list_editable = ("level", "experience", "stat_points", "strength", "dexterity", "constitution", "intelligence") 
    list_display_links = ("user",)  

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profil Gracza"

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)