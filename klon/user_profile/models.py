from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math

class UserProfile(models.Model):
    """
    Model profilu gracza wraz ze statystykami.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    constitution = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    stat_points = models.IntegerField(default=0)
    max_hp = models.IntegerField(default=100)
    hp = models.IntegerField(default=100)
    base_hp = models.IntegerField(default=100)
    defence = models.IntegerField(default=0)
    base_defence = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    base_attack = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    last_regen = models.DateTimeField(default=timezone.now)
    
    def lvlup_exp(self):
        """
        Kalkulacja wymaganego expa do następnego poziomu.
        """
        return math.floor(100 * (self.level ** 1.5))
    
    def dodaj_exp(self, exp):
        """
        Dodawanie expa i ewentualne podnoszenie poziomu.
        """
        self.experience += exp
        while self.experience >= self.lvlup_exp():
            self.experience -= self.lvlup_exp()
            self.lvlup()
        self.save()
        
    def lvlup(self):
        """
        Podnoszenie poziomu i dodawanie wolnych pkt statystyk.
        """
        self.level += 1
        self.stat_points += 5
        self.save()
        
    def hp_regen(self):
        """
        Pasywny hp regen na podtawie bud. fiz. i inteligencji.
        """
        regen_timer = timezone.now() - self.last_regen
        regen_minutes = regen_timer.total_seconds() / 60 
        regen_amount = math.floor((self.intelligence/2 + self.constitution/10) * round(regen_minutes))
        new_hp = self.hp + regen_amount
        if new_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = round(new_hp)
        if regen_amount > 0 or self.hp == self.max_hp:
            self.last_regen = timezone.now()
        self.save()
        
    def __str__(self):
        """
        Zwraca nazwę użytkownika gracza.
        """
        return self.user.username
