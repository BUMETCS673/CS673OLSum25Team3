from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer


def appointments_page(request):
    return render(request, "appointments_view.html")


"""
@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-08
Modified by: Adriel Domingo
Modifications:
Verified:  reviewed
"""

# REST API endpoints
@api_view(['GET'])
def appointments_api(request):
    """
    API endpoint that returns a list of all appointments.
    """
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


