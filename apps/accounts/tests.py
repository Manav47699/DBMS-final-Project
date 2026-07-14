"""
Authentication tests.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_login_page_loads(self):
        resp = self.client.get(reverse('accounts:login'))
        self.assertEqual(resp.status_code, 200)

    def test_login_valid(self):
        resp = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertRedirects(resp, reverse('dashboard'))

    def test_login_invalid(self):
        resp = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'wrongpass',
        })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Invalid')

    def test_logout(self):
        self.client.login(username='testuser', password='testpass123')
        resp = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(resp, reverse('accounts:login'))
