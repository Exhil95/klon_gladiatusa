from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math

class UserProfile(models.Model):
    """
    Model profilu gracza wraz ze statystykami.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Statystyki bazowe i aktualne
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    constitution = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    stat_points = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    # Punkty życia i stamina
    max_hp = models.IntegerField(default=100)
    hp = models.IntegerField(default=100)
    base_hp = models.IntegerField(default=100)
    max_stamina = models.IntegerField(default=10)
    stamina = models.IntegerField(default=10)

    # Statystyki walki
    attack = models.IntegerField(default=3)
    base_attack = models.IntegerField(default=3)
    defence = models.IntegerField(default=3)
    base_defence = models.IntegerField(default=3)

    # Statystyki bazowe do rozwoju
    base_strength = models.IntegerField(default=1)
    base_dexterity = models.IntegerField(default=1)
    base_constitution = models.IntegerField(default=1)
    base_intelligence = models.IntegerField(default=1)

    # Timery regeneracji
    last_regen = models.DateTimeField(default=timezone.now)
    last_regen_stm = models.DateTimeField(default=timezone.now)

    def lvlup_exp(self):
        """Kalkulacja wymaganego expa do następnego poziomu."""
        return math.floor(100 * (self.level ** 1.5))

    def dodaj_exp(self, exp):
        """Dodawanie expa i ewentualne podnoszenie poziomu."""
        self.experience += exp
        while self.experience >= self.lvlup_exp():
            self.experience -= self.lvlup_exp()
            self.lvlup()
        self.save()

    def lvlup(self):
        """Podnoszenie poziomu i dodawanie wolnych pkt statystyk."""
        self.level += 1
        self.stat_points += 5
        self.hp = self.max_hp
        self.stamina = self.max_stamina
        self.save()

    def hp_regen(self):
        """Pasywny hp regen na podstawie bud. fiz. i inteligencji."""
        regen_timer = timezone.now() - self.last_regen
        regen_minutes = regen_timer.total_seconds() / 60
        regen_amount = math.floor((self.intelligence + self.constitution / 2) * round(regen_minutes))
        new_hp = self.hp + regen_amount
        if new_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = round(new_hp)
        if regen_amount > 0 or self.hp == self.max_hp:
            self.last_regen = timezone.now()
        self.save()

    def stamina_regen(self):
        """Pasywny stamina regen na podstawie inteligencji."""
        regen_timer = timezone.now() - self.last_regen_stm
        regen_minutes = regen_timer.total_seconds() / 60
        regen_amount = math.floor((self.intelligence / 2) * round(regen_minutes))
        new_stamina = self.stamina + regen_amount
        if new_stamina > self.max_stamina:
            self.stamina = self.max_stamina
        else:
            self.stamina = round(new_stamina)
        if regen_amount > 0 or self.stamina == self.max_stamina:
            self.last_regen_stm = timezone.now()
        self.save()

    def equipped_items(self):
        from inventory.models import InventoryItem
        return InventoryItem.objects.filter(user=self.user, equipped=True)

    # Bonusy z przedmiotów
    def item_strength_bonus(self):
        return sum(i.item.item_strength for i in self.equipped_items())

    def item_dexterity_bonus(self):
        return sum(i.item.item_dexterity for i in self.equipped_items())

    def item_constitution_bonus(self):
        return sum(i.item.item_constitution for i in self.equipped_items())

    def item_intelligence_bonus(self):
        return sum(i.item.item_intelligence for i in self.equipped_items())

    def item_attack_bonus(self):
        return sum(i.item.dmg for i in self.equipped_items())

    def item_hp_bonus(self):
        return self.item_constitution_bonus() * 25

    def update_stats(self):
        """Aktualizuje statystyki gracza na podstawie bazowych i przedmiotów."""
        self.strength = self.base_strength + self.item_strength_bonus()
        self.dexterity = self.base_dexterity + self.item_dexterity_bonus()
        self.constitution = self.base_constitution + self.item_constitution_bonus()
        self.intelligence = self.base_intelligence + self.item_intelligence_bonus()
        self.attack = self.base_attack + self.item_attack_bonus()
        self.defence = self.base_defence + self.item_dexterity_bonus()
        self.max_hp = self.base_hp + self.item_hp_bonus()
        self.save()

    def __str__(self):
        """Zwraca nazwę użytkownika gracza."""
        return self.user.username
