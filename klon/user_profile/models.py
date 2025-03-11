from django.db import models
from django.contrib.auth.models import User
import math
import datetime as dt

class UserProfile(models.Model):
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
    last_regen = models.DateTimeField(default=dt.datetime.now)
    
    def lvlup_exp(self):
        return math.floor(100 * (self.level ** 1.5))
    
    def dodaj_exp(self, exp):
        self.experience += exp
        while self.experience >= self.lvlup_exp():
            self.experience -= self.lvlup_exp()
            self.lvlup()
        self.save()
        
    def lvlup(self):
        self.level += 1
        self.stat_points += 5
        self.save()
        
    def hp_regen(self):
        new_hp = self.hp + (self.constitution * 2) + 10
        regen_timer = round((dt.now()-self.last_regen).total_seconds() / 300) 
        if new_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = new_hp
        self.save()
                
    def __str__(self):
        return self.user.username
