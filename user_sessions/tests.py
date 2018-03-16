from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse


class TestCalls(TestCase):

    def setUp(self):
        self.url = '/register_user'
        self.data = {'username': 'raees', 'password1': 'admin123', 'password2': 'admin123'}
        self.reverse_url = reverse('user_sessions:register_user')

    def test_user_can_signup_successfully(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(username='raees').count(), 1)
        self.assertIsInstance(response, HttpResponseRedirect)

    def test_username_is_unique(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)
        response2 = self.client.post(self.reverse_url, self.data)
        self.assertEqual(response2.status_code, 200)
        self.assertFormError(response2, 'form', self.data, 'A user with that username already exists.')

    def test_password_restrictions(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)

    def test_empty_fields(self):
        pass

    def test_passwords_did_not_match(self):
        pass
