from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

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


class MFASecurityFlowTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'secureuser'
        self.password = 'securepass123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.mfa_url = reverse('mfa_verify')
        self.dashboard_url = reverse('dashboard')

    def test_cannot_access_dashboard_without_login(self):
        response = self.client.get(self.dashboard_url)
        self.assertRedirects(response, f"{reverse('mlogin')}?next={self.dashboard_url}")

    def test_cannot_access_mfa_verify_without_session(self):
        response = self.client.get(self.mfa_url)
        self.assertRedirects(response, reverse('mlogin'))
