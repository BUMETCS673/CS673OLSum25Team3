"""

@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-08
Modified by: Adriel Domingo
Modifications:
Verified:  reviewed
"""

from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'