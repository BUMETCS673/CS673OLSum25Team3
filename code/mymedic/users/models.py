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

# Create your models here.
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
    

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    reason = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} - {self.patient_name} with {self.doctor_name}"