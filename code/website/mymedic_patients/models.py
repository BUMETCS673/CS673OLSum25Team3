"""
This file holds the models for MyMedic patients
"""
from django.db import models

class Patient(models.Model):
    """
    Model representing patient personal information.

    @ai-generated
    Tool: GitHub Copilot
    Prompt: N/A
    Generated on: 2025-06-01
    Modified by: Tyler Gonsalves
    Modifications: Added fields for phone number, date of birth, dependents.
    Verified:  Unit tested, reviewed
    """
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='patients',
        verbose_name='User'
    )
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(unique=True, verbose_name='Email Address', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Phone Number')
    date_of_birth = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    dependents = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='dependents_of',
        verbose_name='Dependents'
    )