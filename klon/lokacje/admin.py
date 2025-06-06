from django.contrib import admin
from .models import Enemy, Location
from django.utils.html import format_html



@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "colored_type", "lvl", "base_strenght", "base_intelect", 
        "base_dexterity", "base_constitution", "gold_drop", "base_hp", 
        "base_attack", "base_defence", "created_at", "updated_at", "loot_table_display", "drop_chance"
    )
    list_filter = ("type", "lvl", "name")
    search_fields = ("name", "description")
    ordering = ("-id",)
    list_editable = (
        "name", "lvl", "base_strenght", "base_intelect", 
        "base_dexterity", "base_constitution", "gold_drop", "base_hp", 
        "base_attack", "base_defence", "drop_chance"
    )
    list_display_links = ("id",)
    readonly_fields = ("created_at", "updated_at")
    fields = (
        "name", "description", "type", "lvl", "base_strenght", 
        "base_intelect", "base_dexterity", "base_constitution", 
        "gold_drop", "base_hp", "base_attack", "base_defence", 
        "loot_table", "created_at", "updated_at", "drop_chance"
    )
    filter_horizontal = ("loot_table",)

    def save_model(self, request, obj, form, change):
        obj.calculate_stats()  # automatyczne przeliczenie statystyk
        super().save_model(request, obj, form, change)

    @admin.display(description="Loot Table")
    def loot_table_display(self, obj):
        return ", ".join(e.name for e in obj.loot_table.all())

    @admin.display(description="Typ", ordering="type")
    def colored_type(self, obj):
        color = {
            "boss": "red",
            "elite": "orange",
            "normal": "green"
        }.get(obj.type, "black")
        return format_html(f'<span style="color: {color}; font-weight: bold;">{obj.get_type_display()}</span>')

    
      
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Customowy AdminPanel dla lokacji
    """
    
    list_display = ("id", "name", "enemies_display")
    list_filter = ("id", "name")
    search_fields = ("name", "enemies__name")
    ordering = ("-id",)
    list_editable = ("name",)
    list_display_links = ("id",)
    fields = ("name", "enemies")
    filter_horizontal = ("enemies",)
    
    def enemies_display(self, obj):
        """ 
        Metoda pozwalająca na prawidłowe wyświetlanie w AdminPanelu relacji ManyToMany
        """
        return ", ".join(e.name for e in obj.enemies.all())
    
    enemies_display.short_description = "Enemies"


