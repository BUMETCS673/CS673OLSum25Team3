"""This module registers the user models with django"""
from django.contrib import admin
from .models import Patient
from .models import Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)