from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Zaawansowany panel admina dla przedmiotów.
    """
    list_display = (
        "id", "name", "item_type", "rarity", "slot", "item_level", 
        "value", "item_strength", "item_dexterity", 
        "item_constitution", "item_intelligence", 
        "dmg", "dmg_max", "dmg_min", "effect_value"
    )
    list_filter = ("item_type", "rarity", "slot")
    list_editable = (
        "name", "item_type", "rarity", "slot", "item_level", "value",
        "item_strength", "item_dexterity", "item_constitution", 
        "item_intelligence", "dmg", "dmg_max", "dmg_min", "effect_value"
    )
    search_fields = ("name", "description")
    ordering = ("-id",)
    list_display_links = ("id",)

    readonly_fields = ("dmg_min", "dmg_max")  

    fieldsets = (
        ("Podstawowe", {
            "fields": ("name", "description", "item_type", "rarity", "slot", "item_level", "value")
        }),
        ("Statystyki", {
            "fields": ("item_strength", "item_dexterity", "item_constitution", "item_intelligence")
        }),
        ("Obrażenia", {
            "fields": ("dmg", "dmg_max", "dmg_min")
        }),
        ("Efekt mikstury", {
            "fields": ("effect_value",)
        }),
    )
