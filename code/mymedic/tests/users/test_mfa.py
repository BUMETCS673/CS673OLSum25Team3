from django.test import TestCase, Client
from django.urls import reverse

class MFATest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "testuser"
        self.password = "Testpass123!"
        self.register_url = reverse("register")
        self.login_url = reverse("mlogin")
        self.verify_url = reverse("verify_mfa")
        self.dashboard_url = reverse("dashboard")

        self.client.post(self.register_url, {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "firstname": "Test",
            "lastname": "User",
            "email": "test@example.com"
        })

        self.client.post(self.login_url, {
            "username": self.username,
            "password": self.password
        })

    def test_correct_mfa_code_redirects_to_dashboard(self):
        session = self.client.session
        session["mfa_code"] = "123456"
        session.save()

        response = self.client.post(self.verify_url, {
            "mfa_code": "123456"
        })
        self.assertRedirects(response, self.dashboard_url)

    def test_wrong_mfa_code_shows_error(self):
        self.client.login(username='testuser', password='testpass')
        session = self.client.session
        session['expected_mfa_code'] = '123456'
        session.save()

        response = self.client.post('/verify_mfa/', {'mfa_code': 'wrongcode'}, follow=True)
        self.assertContains(response, "Incorrect code")
