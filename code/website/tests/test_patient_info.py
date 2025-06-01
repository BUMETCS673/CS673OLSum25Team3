"""
Unit tests for the patient info module.

@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-01
Modified by: Tyler Gonsalves
Modifications: Added steps to inject user, fixed assertions for validating patient
               info, added docstrings
Verified:  Unit tested, reviewed
"""
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from mymedic_patients.models import Patient

# Test: Patient info created upon user sign up
@pytest.mark.django_db
def test_patient_info_created(client):
    """Tests triggering patient info creation upon user registration."""
    resp = client.post(
        reverse("register"),
        {
            "username": "newuser", 
            "password": "newpass123",
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@example.com"
        },
        content_type="application/json"
    )
    assert resp.status_code == 201 or resp.status_code == 200
    assert (Patient.objects.filter(email="janedoe@example.com").exists()) is True

class TestPatientInfo(TestCase):
    """Tests for CRUD operations on Patient model."""
    def test_create(self):
        test_user = get_user_model().objects.create_user(
            username="testuser", 
            password="testpass123"
        )
        entry = Patient.objects.create(
            user=test_user,
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com"
        )
        self.assertEqual(entry.first_name, "John")
        self.assertEqual(entry.last_name, "Doe")
        self.assertEqual(entry.email, "johndoe@example.com")
        self.assertTrue(Patient.objects.filter(user=test_user).exists())

    def test_update(self):
        test_user = get_user_model().objects.create_user(
            username="testuser2", 
            password="testpass123"
        )
        entry = Patient.objects.create(
            user=test_user,
            first_name="Jane",
            last_name="Doe",
            email="jane_doe@example.com"
        )
        entry.first_name = "Janet"
        entry.save()
        self.assertTrue(Patient.objects.filter(first_name="Janet").exists())
    
    def test_delete(self):
        test_user = get_user_model().objects.create_user(
            username="testuser3", 
            password="testpass123"
        )
        entry = Patient.objects.create(
            user=test_user,
            first_name="John",
            last_name="Doe",
            email="john_doe@example.com"
        )
        entry.delete()
        self.assertFalse(Patient.objects.filter(user=test_user).exists())

