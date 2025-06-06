from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils import timezone

class UserProfileModelTests(TestCase):
    """
    Testy modelu UserProfile.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        UserProfile.objects.filter(user=self.user).delete()
        self.profile = UserProfile.objects.create(user=self.user)

    def test_lvlup_exp(self):
        """Test kalkulacji wymaganego expa do następnego poziomu."""
        self.profile.level = 1
        self.assertEqual(self.profile.lvlup_exp(), 100)
        self.profile.level = 2
        self.assertEqual(self.profile.lvlup_exp(), 282)
        print("test_lvlup_exp zakończony sukcesem")

    def test_dodaj_exp(self):
        """Test dodawania expa i ewentualnego podnoszenia poziomu."""
        self.profile.level = 1
        self.profile.experience = 0
        self.profile.dodaj_exp(150)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.level, 2)
        self.assertEqual(self.profile.experience, 50)
        print("test_dodaj_exp zakończony sukcesem")

    def test_lvlup(self):
        """Test podnoszenia poziomu i dodawania wolnych pkt statystyk."""
        self.profile.level = 1
        self.profile.stat_points = 0
        self.profile.lvlup()
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.level, 2)
        self.assertEqual(self.profile.stat_points, 5)
        print("test_lvlup zakończony sukcesem")

    def test_hp_regen(self):
        """Test regeneracji HP."""
        self.profile.hp = 50
        self.profile.constitution = 10
        self.profile.intelligence = 10
        self.profile.last_regen = timezone.now() - timezone.timedelta(minutes=10)
        self.profile.hp_regen()
        self.profile.refresh_from_db()
        self.assertGreater(self.profile.hp, 50)
        self.assertLessEqual(self.profile.hp, self.profile.max_hp)
        print(f"test_hp_regen zakończony sukcesem z ilością hp: {self.profile.hp}")
