from django.db import models

class Enemy(models.Model):
    
    name = models.CharField(max_length=25, default="test_object")
    lvl = models.IntegerField(default=1)
    base_strenght = models.IntegerField(default=1)
    base_intelect = models.IntegerField(default=1)
    base_dexterity = models.IntegerField(default=1)
    base_constitution = models.IntegerField(default=1)
    gold_drop = models.IntegerField(default=0)
    base_hp = models.IntegerField(default=100)
    base_attack = models.IntegerField(default=0)
    base_defence = models.IntegerField(default=0)
    #loot_table = models.ManyToManyField()
    
    def __str__(self):
        return self.name
    
    