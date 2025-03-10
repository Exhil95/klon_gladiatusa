from django.db import models
from django.contrib.auth.models import User
import math

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    constitution = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    stat_points = models.IntegerField(default=0)
    
    
    def lvlup_exp(self):
        return math.floor(100 * (self.level ** 1.5))
    
    def dodaj_exp(self, exp):
        self.experience += exp
        while self.experience >= self.lvlup_exp():

            self.experience -= self.lvlup_exp()
        self.save()
        
    def lvlup(self):
        self.level += 1
        self.stat_points += 5
        self.save()
                
    def __str__(self):
        return self.user.username
    