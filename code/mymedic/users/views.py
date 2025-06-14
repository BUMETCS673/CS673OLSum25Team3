"""
Views for rendering the registration, login, dashboard, profile, and logout.

@ai-generated
Tool: GitHub Copilot
Generated on: 06-08-2025
Modified by: Tyler Gonsalves
Modifications: Added error handling, function decorators and updated docstrings
Verified: ✅ Unit tested, reviewed
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserUpdateForm
from .models import Patient

def register(request):
    """
    Handle user registration.
    """
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Patient.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['firstname'],
                last_name=form.cleaned_data['lastname'],
                email=form.cleaned_data['email'],
                date_of_birth=None
            )
            return redirect("mlogin")
        else:
            messages.error(request, "Invalid registration credentials")
    return render(request, 'users/register.html', {'form': form})

def mlogin(request):
    """
    Handle user login.
    """
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect("dashboard")
            messages.error(request, "Invalid credentials")
            return redirect("mlogin")
        messages.error(request, "Invalid credentials")
        return redirect("mlogin")
    return render(request, 'users/login.html', {'form': form})

def mlogout(request):
    """
    Log out the current user and redirect to login.
    """
    logout(request)
    return redirect("mlogin")

@login_required(login_url='mlogin')
def dashboard(request):
    """
    Display user dashboard.
    """
    return render(request, 'users/dashboard.html')

@login_required(login_url='mlogin')
def profile(request):
    """
    Show and update user profile.
    """
    user = request.user
    patient_data = Patient.objects.filter(username=user.username).first()
    user_data = User.objects.filter(username=user.username).first()

    if not patient_data:
        return HttpResponse("Patient data not found", status=404)

    form = CustomUserUpdateForm(initial={
        "firstname": patient_data.first_name,
        "lastname": patient_data.last_name,
        "email": patient_data.email,
        "phone": patient_data.phone_number,
        "birth_date": patient_data.date_of_birth
    })

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST)
        if form.is_valid():
            patient_data.first_name = form.cleaned_data.get("first_name", patient_data.first_name)
            patient_data.last_name = form.cleaned_data.get("last_name", patient_data.last_name)
            patient_data.email = form.cleaned_data.get("email", patient_data.email)
            patient_data.phone_number = form.cleaned_data.get("phone", patient_data.phone_number)
            patient_data.date_of_birth = form.cleaned_data.get("birth_date", patient_data.date_of_birth)

            user_data.first_name = form.cleaned_data.get("first_name", user_data.first_name)
            user_data.last_name = form.cleaned_data.get("last_name", user_data.last_name)
            user_data.email = form.cleaned_data.get("email", user_data.email)

            patient_data.save()
            user_data.save()
            return redirect("profile")

    return render(request, 'users/profile.html', {"form": form})


# ──────────────── Medical Records View ────────────────
@login_required(login_url='mlogin')
def medical_records(request):
    """
    Render the static medical records page for patients.
    """
    return render(request, 'users/medical_records.html')
