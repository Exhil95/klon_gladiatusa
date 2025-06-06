from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "item", "item_type", "item_slot", "equipped"
    )
    list_filter = ("equipped", "item__item_type", "item__slot", "user")
    list_editable = ("equipped",)
    search_fields = ("user__username", "item__name")
    ordering = ("-id",)

    @admin.display(description="Typ")
    def item_type(self, obj):
        return obj.item.item_type

    @admin.display(description="Slot")
    def item_slot(self, obj):
        return obj.item.slot
