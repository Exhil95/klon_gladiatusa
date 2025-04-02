from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Enemy, Location


@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    """
    Customowy AdminPanel dla Wrogów
    """
    # Pola wyświetlane w widoku listy obiektów
    list_display = (
        "id", "name", "type", "lvl", "base_strenght", "base_intelect", 
        "base_dexterity", "base_constitution", "gold_drop", "base_hp", 
        "base_attack", "base_defence", "created_at", "updated_at"
    )
    # Filtry w widoku listy obiektów
    list_filter = ("type", "lvl", "name")
    # Pola, po których można wyszukiwać
    search_fields = ("name", "description")
    # Kolejność wyświetlania obiektów
    ordering = ("-id",)
    # Pola edytowalne w widoku listy obiektów
    list_editable = (
        "name", "type", "lvl", "base_strenght", "base_intelect", 
        "base_dexterity", "base_constitution", "gold_drop", "base_hp", 
        "base_attack", "base_defence"
    )
    # Pola, które można kliknąć, aby przejść do szczegółów obiektu
    list_display_links = ("id",)
    # Pola wyświetlane w widoku szczegółów obiektu
    fields = (
        "name", "description", "type", "lvl", "base_strenght", 
        "base_intelect", "base_dexterity", "base_constitution", 
        "gold_drop", "base_hp", "base_attack", "base_defence", 
        #"loot_table", 
        "created_at", "updated_at"
    )
    # Pola tylko do odczytu (np. pola automatyczne)
    readonly_fields = ("created_at", "updated_at")
    
      
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
    
     
