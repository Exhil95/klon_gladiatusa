from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "item", "equipped")
    list_filter = ("user", "equipped")
    list_editable = ("equipped",)
    search_fields = ("user__username", "item__name")