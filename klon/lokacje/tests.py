from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Enemy


class LocationViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="fighter", password="pass12345")
        self.client.login(username="fighter", password="pass12345")

    def test_map_view_uses_fallback_names_when_locations_are_missing(self):
        response = self.client.get(reverse("mapa"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Zdziczale Lochy")


class FightViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="fighter", password="pass12345")
        self.profile = self.user.userprofile
        self.profile.attack = 20
        self.profile.defence = 0
        self.profile.hp = 50
        self.profile.stamina = 5
        self.profile.experience = 0
        self.profile.gold = 0
        self.profile.save()
        self.client.login(username="fighter", password="pass12345")

    @patch("lokacje.views.random.random", return_value=1.0)
    def test_winning_fight_awards_experience_through_leveling_logic(self, _random):
        self.profile.experience = 95
        self.profile.save()
        enemy = Enemy.objects.create(
            name="Training Dummy",
            lvl=10,
            base_hp=1,
            base_attack=0,
            base_defence=0,
            gold_drop=7,
        )

        response = self.client.post(reverse("fight", args=[enemy.id]), {"strategy": "balanced"})

        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.level, 2)
        self.assertEqual(self.profile.experience, 95)
        self.assertEqual(self.profile.gold, 7)
        self.assertEqual(self.profile.hp, self.profile.max_hp)
        self.assertEqual(self.profile.stamina, self.profile.max_stamina - 1)
        self.assertContains(response, "100 expa")

    @patch("lokacje.views.random.random", return_value=1.0)
    def test_losing_fight_with_zero_hp_applies_death_penalty(self, _random):
        self.profile.attack = 0
        self.profile.hp = 5
        self.profile.stamina = 3
        self.profile.experience = 100
        self.profile.save()
        enemy = Enemy.objects.create(
            name="Arena Brute",
            lvl=1,
            base_hp=999,
            base_attack=50,
            base_defence=999,
            gold_drop=0,
        )

        response = self.client.post(reverse("fight", args=[enemy.id]), {"strategy": "balanced"})

        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.hp, 1)
        self.assertEqual(self.profile.stamina, 2)
        self.assertEqual(self.profile.experience, 95)
        self.assertContains(response, "Utracono 5 expa")
