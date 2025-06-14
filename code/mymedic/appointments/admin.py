from django.contrib import admin

# Register your models here.

from .models import Appointment
admin.site.register(Appointment)
