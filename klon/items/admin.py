from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Customowy AdminPanel dla przedmiotów
    """
    list_display = (
        "id", "name", "item_type", "rarity", "slot", "item_level", 
        "value", "item_strength", "item_dexterity", 
        "item_constitution", "item_intelligence", 
        "dmg", "dmg_max", "dmg_min", "effect_value"
    )
    list_filter = ("rarity", "slot", "item_type")
    search_fields = ("name", "description")
    ordering = ("-id",)
    list_editable = (
        "name", "item_type", "rarity", "slot", "item_level", "value",
        "item_strength", "item_dexterity", "item_constitution", 
        "item_intelligence", "dmg", "dmg_max", "dmg_min", "effect_value"
    )
    list_display_links = ("id",)
    fields = (
        "name", "description", "item_type", "rarity", "slot", 
        "item_level", "value", "item_strength", "item_dexterity", 
        "item_constitution", "item_intelligence", "dmg", 
        "dmg_max", "dmg_min", "effect_value"
    )
