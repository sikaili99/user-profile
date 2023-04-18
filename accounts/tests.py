from django.test import Client, TestCase
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.urls import reverse

from accounts.models import Profile


class TestViews(TestCase):

    def setUp(self):
        """
        Set up necessary data for the tests.
        """
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.logout_url = reverse('accounts:logout')
        self.register_url = reverse('accounts:signup')
        self.obj = User.objects.create_user(
            username='test', email='abc@gmail.com', first_name='mateo', last_name='sikaili', password="password")

    def test_register_post(self):
        """
        Test registration view with POST request.
        """
        response = self.client.post(self.register_url, {
            'first_name': 'Test User',
            'last_name': 'Tester',
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertEquals(response.status_code, 302)

        # Check if user profile is created through django signals on registration
        self.assertTrue(Profile.objects.filter(
            user__username='testuser').exists())

        # Check if user profile has the correct data
        profile = Profile.objects.get(user__username='testuser')
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.home_address, '')
        self.assertEqual(profile.phone_number, '')
        # Compare x coordinate (efault)
        self.assertEqual(profile.location.x, 1.0)
        # Compare y coordinate (efault)
        self.assertEqual(profile.location.y, 1.0)

    def test_login_post(self):
        """
        Test login view with POST request.
        """
        response = self.client.post(self.login_url, {
            'username': 'test',
            'password': 'password',
        })
        self.assertEquals(response.status_code, 302)

    def test_logout_successful(self):
        """
        Test successful logout.
        """
        self.client.login(email='testuser@gmail.com', password='testpassword')
        response = self.client.post(self.logout_url)
        self.assertEquals(response.status_code, 302)

    def test_logout_redirect(self):
        """
        Test logout view with redirect.
        """
        self.client.login(email='testuser@gmail.com', password='testpassword')
        response = self.client.post(self.logout_url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
