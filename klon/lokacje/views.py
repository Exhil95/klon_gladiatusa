from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Enemy, Location
import random
from inventory.models import InventoryItem
from django.template.loader import render_to_string
from django.http import HttpResponse
from user_profile.models import UserProfile


LOCATION_SLOTS = [
    (1, "location1", "Zdziczale Lochy"),
    (2, "location2", "Cyrk Gladiatorow"),
    (3, "location3", "Pustynne Wzgorza"),
    (4, "location4", "Rowniny"),
]

# Widoki lokacji
def mapa_view(request):
    locations = Location.objects.in_bulk([slot[0] for slot in LOCATION_SLOTS])
    context = {
        context_name: locations.get(location_id) or {"name": fallback_name}
        for location_id, context_name, fallback_name in LOCATION_SLOTS
    }
    return render(request, 'lokacje/mapa.html', context)


def _location_view(request, location_id, template_name):
    location = get_object_or_404(Location, id=location_id)
    enemies = location.enemies.all()
    return render(request, template_name, {'location': location, 'enemies': enemies})


def beast_dung_view(request):
    return _location_view(request, 1, 'lokacje/beast_dung.html')

def circus_view(request):
    return _location_view(request, 2, 'lokacje/circus.html')

def dessert_hills_view(request):
    return _location_view(request, 3, 'lokacje/dessert_hills.html')

def plains_view(request):
    return _location_view(request, 4, 'lokacje/plains.html')

# Silnik walki
class BattleEngine:
    def __init__(self, user_profile, enemy, strategy):
        self.user = user_profile
        self.enemy = enemy
        self.strategy = strategy
        self.log = []
        self.result = None

    def calculate_modifiers(self):
        if self.strategy == 'aggressive':
            return 1.05, 1.10
        elif self.strategy == 'defensive':
            return 0.95, 0.90
        return 1.0, 1.0

    def simulate(self):
        atk_mod, def_mod = self.calculate_modifiers()
        user_hp = self.user.hp
        enemy_hp = self.enemy.base_hp
        user_total_dmg = 0
        enemy_total_dmg = 0

        for round_num in range(1, 21):
            self.log.append(f"Tura {round_num}")

            # Gracz atakuje
            dmg = max(0, self.user.attack * atk_mod - self.enemy.base_defence)
            if random.random() < 0.1:
                dmg *= 2
                self.log.append("🔥 Trafienie krytyczne!")
            dmg = int(dmg)
            enemy_hp -= dmg
            user_total_dmg += dmg
            self.log.append(f"Zadałeś {dmg} obrażeń wrogowi ({max(enemy_hp, 0)} HP).")

            if enemy_hp <= 0:
                self.result = 'win'
                return user_hp, enemy_hp, self.result, self.log

            # Wróg kontratakuje
            enemy_dmg = max(0, self.enemy.base_attack - self.user.defence * def_mod)
            if random.random() < 0.05:
                self.log.append("🛡️ Zablokowałeś atak przeciwnika!")
                enemy_dmg = 0
            elif random.random() < 0.05:
                self.log.append("💨 Uniknąłeś ataku przeciwnika!")
                enemy_dmg = 0

            enemy_dmg = int(enemy_dmg * def_mod)
            user_hp -= enemy_dmg
            enemy_total_dmg += enemy_dmg
            self.log.append(f"Otrzymałeś {enemy_dmg} obrażeń ({max(user_hp, 0)} HP).")

            if user_hp <= 0:
                self.result = 'lose'
                return user_hp, enemy_hp, self.result, self.log

        self.log.append("🔚 Limit 20 tur osiągnięty.")
        if user_total_dmg >= enemy_total_dmg:
            self.log.append("📊 Wygrałeś dzięki większym obrażeniom.")
            self.result = 'win'
        else:
            self.log.append("📊 Przegrałeś – przeciwnik zadał więcej obrażeń.")
            self.result = 'lose'
        return user_hp, enemy_hp, self.result, self.log

# Widok walki
@login_required
def fight_view(request, enemy_id):
    enemy = get_object_or_404(Enemy, id=enemy_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_profile.stamina_regen()

    if user_profile.stamina < 1:
        return render(request, 'lokacje/fight_result_partial.html', {
            'log': ["❌ Nie masz wystarczającej staminy, aby rozpocząć walkę!"],
            'result': 'fail',
            'enemy': enemy,
            'enemy_hp': enemy.base_hp,
            'enemy_max_hp': enemy.base_hp,
        })

    if request.method == 'POST':
        strategy = request.POST.get('strategy', 'balanced')
        engine = BattleEngine(user_profile, enemy, strategy)
        remaining_hp, enemy_hp, result, log = engine.simulate()
        enemy_hp = max(0, enemy_hp)
        enemy_hp_percentage = int((enemy_hp / enemy.base_hp) * 100) if enemy.base_hp else 0


        leveled_up = False

        if result == 'win':
            exp_reward = enemy.lvl * 10
            level_before_reward = user_profile.level
            user_profile.gold += enemy.gold_drop
            user_profile.dodaj_exp(exp_reward)
            leveled_up = user_profile.level > level_before_reward
            log.append(f"🏆 Wygrałeś! Zdobyto {enemy.gold_drop} złota i {exp_reward} expa.")

            loot_items = list(enemy.loot_table.all())
            if loot_items and random.random() < float(enemy.drop_chance):
                dropped_item = random.choice(loot_items)
                InventoryItem.objects.create(
                    user=request.user,
                    item=dropped_item
                )
                log.append(f"🎁 Znalazłeś przedmiot: {dropped_item.name}!")
            else:
                log.append("🔎 Tym razem nie znalazłeś żadnego przedmiotu.")
        elif result == 'lose' and remaining_hp <= 0:
            user_profile.hp = 1
            penalty = int(user_profile.experience * 0.05)
            user_profile.experience = max(0, user_profile.experience - penalty)
            log.append(f"💀 Przegrałeś i zginąłeś! HP ustawiono na 1. Utracono {penalty} expa.")
        else:
            log.append("⚠️ Przegrałeś walkę, ale przetrwałeś – bez strat.")

        user_profile.hp = max(1, remaining_hp, user_profile.hp if leveled_up else 1)
        user_profile.stamina = max(0, user_profile.stamina - 1)
        user_profile.save()

        return render(request, 'lokacje/fight_result_partial.html', {
            'log': log,
            'result': result,
            'enemy': enemy,
            'enemy_hp': enemy_hp,
            'enemy_max_hp': enemy.base_hp,
            'enemy_hp_percentage': enemy_hp_percentage,
        })


    return render(request, 'lokacje/fight.html', {
        'user_profile': user_profile,
        'enemy': enemy,
    })

@login_required
def refresh_banner(request):
    player = UserProfile.objects.get(user=request.user)
    html = render_to_string("banner_up.html", {"player": player})
    return HttpResponse(html)
