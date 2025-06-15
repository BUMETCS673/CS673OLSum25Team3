from django.test import TestCase, Client
from django.contrib.auth.models import User
from users.models import Appointment
from django.urls import reverse
from datetime import date

class AppointmentTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.appointment = Appointment.objects.create(
            user=self.user,
            patient_name='testuser',
            doctor_name='Dr. House',
            date=date.today(),
            reason='Annual Checkup'
        )

    def test_appointment_shows_on_dashboard(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dr. House')
        self.assertContains(response, 'Annual Checkup')

    def test_cancel_appointment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('cancel_appointment', args=[self.appointment.id]))
        self.assertRedirects(response, reverse('dashboard'))
        self.assertFalse(Appointment.objects.filter(id=self.appointment.id).exists())