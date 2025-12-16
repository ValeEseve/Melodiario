from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def setUp(self):
        self.password = 'StrongPass123!'
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password=self.password,
        )

    def test_login_success_redirects_to_dashboard(self):
        response = self.client.post(
            reverse('users:login'),
            {'username': self.user.username, 'password': self.password},
            follow=True,
        )

        self.assertRedirects(response, reverse('users:dashboard'))
        self.assertTrue(response.context['user'].is_authenticated)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Has iniciado sesión correctamente." in str(message) for message in messages))

    def test_login_failure_shows_error_and_stays_on_page(self):
        response = self.client.post(
            reverse('users:login'),
            {'username': self.user.username, 'password': 'wrongpass'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTrue(response.context['form'].errors)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("incorrectos" in str(message) for message in messages))
