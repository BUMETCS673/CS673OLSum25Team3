from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Appointment
from .serializers import AppointmentSerializer

# HTML pages
def login_page(request):
    return render(request, "login.html")

def signup_page(request):
    return render(request, "signup.html")

def dashboard(request):
    return render(request, "dashboard.html")

def appointments_view(request):
    return render(request, "appointments_view.html")


# REST API endpoints
@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)
    User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully"})

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['GET'])
def appointment_list(request):
    """
    List all appointments.
    """
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)
