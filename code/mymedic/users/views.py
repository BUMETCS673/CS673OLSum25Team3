"""
Views for rendering the registration, sign up, and dashboard, and a logout API endpoint

@ai-generated
Tool: GitHub Copilot
Prompt: N/A (Code completion unprompted)
Generated on: 06-08-2025
Modified by: Tyler Gonsalves
Modifications: Added error handling, function decorators and updated docstrings
Verified: ✅ Unit tested, reviewed
*/
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserUpdateForm
from django.contrib.auth.models import User
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
    """
    Render the user registration view.
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

    return render(request, 'users/register.html', context={'form': form})

def mlogin(request):
    """
    Render the user login view.
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
            else:
                messages.error(request, "Invalid credentials")
                return redirect("mlogin")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("mlogin")
    return render(request, 'users/login.html', context={'form': form})

def mlogout(request):
    """
    Handle user logout and redirect to the login page.
    """
    logout(request)
    return redirect("mlogin")

@login_required(login_url='mlogin')
def dashboard(request):
    """
    Render the dashboard view for users.
    """
    return render(request, 'users/dashboard.html')

@login_required(login_url='mlogin')
def profile(request):
    """
    Render the user profile view.
    """
    user = request.user
    try:
        patient_data = Patient.objects.filter(username=user.username).first()
        user_data = User.objects.filter(username=user.username).first()
    except Patient.DoesNotExist:
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
    else:
        return render(request, 'users/profile.html', context={"form": form})

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_GET
def search_records(request):
    """
    API endpoint to search medical records by doctor or prescription.
    """
    query = request.GET.get("q", "").lower()

    # Sample static data for mock search
    sample_data = [
        {"doctor": "Dr. Smith", "prescription": "Ibuprofen"},
        {"doctor": "Dr. Lee", "prescription": "Amoxicillin"},
        {"doctor": "Dr. Taylor", "prescription": "Lisinopril"},
    ]

    # Filter results by matching query in doctor or prescription fields
    results = [
        record for record in sample_data
        if query in record["doctor"].lower() or query in record["prescription"].lower()
    ]

    return JsonResponse(results, safe=False)
