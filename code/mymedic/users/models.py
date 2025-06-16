"""
This module holds the user model definitions

@ai-generated
Tool: GitHub Copilot
Prompt: N/A (Code completion unprompted)
Generated on: 06-08-2025
Modified by: Tyler Gonsalves
Modifications: Added docstrings, username field, and allowed null fields for phone and 
               DOB
Verified: ✅ Unit tested, reviewed
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from datetime import timedelta

class Patient(models.Model):
    """Database model for patient information"""
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class MedicalRecord(models.Model):
    """Database Model for patients' medical records history"""
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.date})"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    reason = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} - {self.patient_name} with {self.doctor_name}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)
    prescription = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    dosage = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor} - {self.prescription}"

class PasswordResetToken(models.Model):
    """Password reset tokens with expiry and usage flags"""
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        return not self.is_used and (timezone.now() - self.created_at < timedelta(hours=1))

    def __str__(self):
        return f"ResetToken for {self.user.username} ({'used' if self.is_used else 'active'})"
