"""This module registers the user models with django"""
from django.contrib import admin
from .models import Patient

# Register your models here.
admin.site.register(Patient)