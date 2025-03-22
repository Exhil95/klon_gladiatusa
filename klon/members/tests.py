from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class MembersViewsTestCase(TestCase):
    def setUp(self):
        """
        Przygotowanie środowiska testowego.
        """
        self.client = Client()
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_user_success(self):
        """
        Test poprawnego logowania użytkownika.
        """
        response = self.client.post(reverse('login_user'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('profil'))

    def test_login_user_failure(self):
        """
        Test nieudanego logowania użytkownika.
        """
        response = self.client.post(reverse('login_user'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertRedirects(response, reverse('login_user'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Błąd przy logowaniu, spróbuj ponownie")

    def test_logout_user(self):
        """
        Test wylogowania użytkownika.
        """
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout_user'))
        self.assertRedirects(response, reverse('login_user'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Wylogowano")

    def test_register_user_success(self):
        """
        Test poprawnej rejestracji użytkownika.
        """
        response = self.client.post(reverse('register_user'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertRedirects(response, reverse('profil'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_user_failure(self):
        """
        Test nieudanej rejestracji użytkownika (np. różne hasła).
        """
        response = self.client.post(reverse('register_user'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='newuser').exists())