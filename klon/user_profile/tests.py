from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileModelTests(TestCase):
    """
    Testy modelu UserProfile.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        UserProfile.objects.filter(user=self.user).delete()
        self.profile = UserProfile.objects.create(user=self.user)

    def test_lvlup_exp(self):
        """
        Test kalkulacji wymaganego expa do następnego poziomu.
        """
        self.profile.level = 1
        self.assertEqual(self.profile.lvlup_exp(), 100)
        self.profile.level = 2
        self.assertEqual(self.profile.lvlup_exp(), 282)
        
    def test_dodaj_exp(self):
        """
        Test dodawania expa i ewentualnego podnoszenia poziomu.
        """ 
        self.profile.level = 1 
        self.profile.experience = 0 
        self.profile.dodaj_exp(150) 
        self.assertEqual(self.profile.level, 2) 
        self.assertEqual(self.profile.experience, 50)
