"""

@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-08
Modified by: Adriel Domingo
Modifications:
Verified:  reviewed
"""

from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListAPIView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer