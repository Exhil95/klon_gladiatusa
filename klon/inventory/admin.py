from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "type", "equipped"
    )
    
    list_filter = (
        "name", "equipped"
    )
    
    search_fields = (
        "name",
    )
    
    ordering = ("-id",)
    
    list_editable = (
        "name", "type", "equipped"
    )
    list_display_links = ("id",)
    
    fields = (
        "name", "type", "equipped"
    )