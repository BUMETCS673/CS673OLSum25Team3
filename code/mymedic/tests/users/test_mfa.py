from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory

class MFAVerificationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.login_url = reverse('mlogin')
        self.mfa_url = reverse('mfa_verify')

    def test_valid_mfa_code(self):
        session = self.client.session
        session['pre_mfa_user_id'] = self.user.id
        session['mfa_code'] = '123456'
        session.save()

        response = self.client.post(self.mfa_url, {'code': '123456'})
        self.assertRedirects(response, reverse('dashboard'))

    def test_invalid_mfa_code(self):
        session = self.client.session
        session['pre_mfa_user_id'] = self.user.id
        session['mfa_code'] = '123456'
        session.save()

        response = self.client.post(self.mfa_url, {'code': '000000'})
        self.assertContains(response, "Invalid code. Please try again.", status_code=200)
