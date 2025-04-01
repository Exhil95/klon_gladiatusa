from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Enemy


@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lvl", "base_strenght", "base_intelect", "base_dexterity", "base_constitution", "gold_drop", "base_hp", "base_attack", "base_defence")
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("-id",)
    fields = list_display
    list_editable = ("name", "lvl", "base_strenght", "base_intelect", "base_dexterity", "base_constitution", "gold_drop", "base_hp", "base_attack", "base_defence")
    list_display_links = ("id",)
    