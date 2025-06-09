from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserUpdateForm
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
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
                
                mfa_code = str(random.randint(100000, 999999))
                request.session['mfa_code'] = mfa_code
                request.session['mfa_verified'] = False

                print("🔐 MFA Code 🔐 :", mfa_code)  

                return redirect("verify_mfa")  
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


def verify_mfa(request):
    if request.method == 'POST':
        input_code = request.POST.get('mfa_code')
        if input_code == request.session.get('mfa_code'):
            request.session['mfa_verified'] = True
            return redirect("dashboard")
        else:
            messages.error(request, "Incorrect code. Please try again.")
            return redirect("verify_mfa")

    return render(request, 'users/verify_mfa.html')


@login_required(login_url='mlogin')
def dashboard(request):
    """
    Render the dashboard view for users.
    """
    if not request.session.get('mfa_verified'):
        return redirect("verify_mfa")
    return render(request, 'users/dashboard.html')

@login_required(login_url='mlogin')
def profile(request):
    """
    Render the user profile view.
    """
    user = request.user
    try:
        patient_data = Patient.objects.filter(username=user.username).first()
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
            form.save()
            return redirect("profile")
    else:
        return render(request, 'users/profile.html', context={"form": form})
    

