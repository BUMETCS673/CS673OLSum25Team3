from django.test import TestCase
from django.urls import reverse

class PrivacyPolicyViewTests(TestCase):
    def test_privacy_policy_page(self):
        url = reverse("privacy_policy")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Privacy Policy")
