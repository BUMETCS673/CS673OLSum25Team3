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
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserUpdateForm
from django.contrib.auth.models import User
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.utils import send_mfa_code
from .forms import MFAForm
from django import forms

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
                request.session['pre_mfa_user_id'] = user.id

                send_mfa_code(user.email, request)
                return redirect("mfa_verify")
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

class MFAForm(forms.Form):
    code = forms.CharField(max_length=6, required=True)


def mfa_verify(request):
    """
    Verify the MFA code sent via email
    """
    form = MFAForm()
    if request.method == 'POST':
        form = MFAForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            user_id = request.session.get('pre_mfa_user_id')

            if not user_id:
                messages.error(request, "Session expired. Please login again.")
                return redirect('mlogin')

            try:
                user = User.objects.get(id=user_id)
                expected_code = request.session.get('mfa_code')  # 
            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('mlogin')

            if code == expected_code:
                login(request, user)
                del request.session['pre_mfa_user_id']
                del request.session['mfa_code']
                return redirect('dashboard')
            else:
                form.add_error('code', 'Invalid code. Please try again.')

    return render(request, 'users/mfa_verify.html', {'form': form})