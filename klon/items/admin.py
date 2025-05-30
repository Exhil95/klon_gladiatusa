from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Customowy AdminPanel dla przedmiotów
    """
    list_display = (
        "id", "name", "rarity", "slot", "item_level", 
         "value"
    )
    list_filter = ("rarity", "slot")
    search_fields = ("name", "description")
    ordering = ("-id",)
    list_editable = ("name", "rarity", "slot", "item_level", "value")
    list_display_links = ("id",)
    fields = (
        "name", "description", "rarity", "slot", 
        "item_level",  "value"
    )