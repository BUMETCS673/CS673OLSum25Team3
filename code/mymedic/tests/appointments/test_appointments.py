"""
@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-15
Modified by: Adriel Domingo
Modifications: datetime spelling and appointments_api url inserted
Verified: reviewed
"""

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from appointments.models import Appointment

User = get_user_model()

@pytest.mark.django_db
def test_appointment_creation():
    appointment = Appointment.objects.create(
        patient_id=1,
        doctor_id=2,
        reason="Checkup",
        status="Scheduled",
        datetime="2025-06-20T10:00:00Z"
    )
    assert appointment.reason == "Checkup"
    assert appointment.status == "Scheduled"

@pytest.mark.django_db
def test_appointments_list_view(client):
    user = User.objects.create_user(username="testuser2", password="testpass2")
    client.login(username="testuser2", password="testpass2")
    Appointment.objects.create(
        patient_id=1,
        doctor_id=2,
        reason="Consultation",
        status="Scheduled",
        datetime="2025-06-21T14:00:00Z"
    )
    url = reverse("appointments_api")  # Change to your actual url name
    response = client.get(url)
    assert response.status_code == 200
    assert b"Consultation" in response.content

