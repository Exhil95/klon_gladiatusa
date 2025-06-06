from django.contrib import admin
from .models import MerchantOffer

@admin.register(MerchantOffer)
class MerchantOfferAdmin(admin.ModelAdmin):
    list_display = (
        "id", "type", "item", "price", "stock", "available_until",
        "is_active", "is_available"
    )
    list_filter = ("type", "available_until")
    search_fields = ("item__name",)
    ordering = ("-available_until",)
    list_editable = ("price", "stock", "available_until")
    list_display_links = ("id", "item")
    readonly_fields = ("is_active", "is_available")
    fields = (
        "type", "item", "price", "stock", "available_until",
        "is_active", "is_available"
    )
