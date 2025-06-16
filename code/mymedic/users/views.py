import json
import logging
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.urls import reverse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from .models import Patient, PasswordResetToken
from .forms import CustomUserUpdateForm
from users.models import Appointment

logger = logging.getLogger(__name__)


@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "users/login.html")


@api_view(['POST'])
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user     = authenticate(username=username, password=password)
    if user:
        django_login(request, user)
        refresh = RefreshToken.for_user(user)
        request.session['access_token'] = str(refresh.access_token)
        return Response({
            "refresh": str(refresh),
            "access":  str(refresh.access_token),
            "username": user.username,
            "full_name": f"{user.first_name} {user.last_name}"
        })
    return Response({"error": "Invalid credentials"}, status=400)


@never_cache
@login_required(login_url='login')
def logout_page(request):
    django_logout(request)
    response = redirect('login')
    response.delete_cookie('sessionid')
    response.delete_cookie('access_token')
    return response


@api_view(['POST'])
def logout_api(request):
    request.session.flush()
    django_logout(request)
    return Response({"message": "Logged out successfully"})


@never_cache
def signup_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "users/register.html")


@api_view(['POST'])
def register(request):
    username   = request.data.get("username")
    password   = request.data.get("password")
    email      = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name  = request.data.get("last_name")
    phone      = request.data.get("phone", "")
    dob        = request.data.get("date_of_birth", None)

    if not all([username, password, email, first_name, last_name]):
        return Response({"error": "Missing required fields"}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username exists"}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({"error": "Email exists"}, status=400)

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        dob_date = None
        if dob:
            try:
                dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
            except ValueError:
                logger.warning(f"Invalid dob: {dob}")
        Patient.objects.create(
            username=user.username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone,
            date_of_birth=dob_date
        )
        if user.email:
            send_mail(
                'Welcome to MyMedic',
                f'Hi {first_name}, thanks for registering!',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True
            )
        return Response({"message": "Account created"})
    except Exception as e:
        user.delete()
        logger.error(f"Register error: {e}")
        return Response({"error": "Failed to create account"}, status=500)


@never_cache
def dashboard(request):
    token = request.COOKIES.get('access_token') or request.session.get('access_token')
    if not token:
        return redirect('login')
    try:
        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        appointments = Appointment.objects.filter(user=user).order_by('date')
        return render(request, "users/dashboard.html", {
            'user': user,
            'appointments': appointments
        })
    except (InvalidToken, TokenError):
        return redirect('login')


@never_cache
def forgot_password_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "users/forgot_password.html")


@api_view(['POST'])
def forgot_password(request):
    identifier = request.data.get("username")
    if not identifier:
        return Response({"error": "Provide username/email"}, status=400)
    try:
        user = User.objects.get(email=identifier) if '@' in identifier \
               else User.objects.get(username=identifier)
        token = PasswordResetToken.objects.create(user=user).token
        reset_url  = request.build_absolute_uri(f"http://localhost:8080/reset-password/?token={token}")
        send_mail(
            'Reset your MyMedic password',
            f'Click here to reset your password:\n\n{reset_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False
        )
        return Response({"message": "Password reset link sent"})
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    except Exception as e:
        logger.error(f"Forgot pw error: {e}")
        return Response({"error": "Failed to send email"}, status=500)


@api_view(['POST'])
def validate_reset_token(request):
    token = request.data.get("token")
    try:
        rt = PasswordResetToken.objects.get(token=token)
        if rt.is_valid():
            return Response({"valid": True})
        return Response({"valid": False, "error": "Token expired or used"}, status=400)
    except PasswordResetToken.DoesNotExist:
        return Response({"valid": False, "error": "Invalid token"}, status=400)


@never_cache
def reset_password_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    token = request.GET.get('token')
    return render(request, "users/reset_password.html", {'token': token})


@api_view(['POST'])
def reset_password(request):
    token    = request.data.get("token")
    new_pass = request.data.get("new_password")
    try:
        rt = PasswordResetToken.objects.get(token=token)
        if not rt.is_valid():
            return Response({"error": "Invalid or expired token"}, status=400)
        user = rt.user
        user.set_password(new_pass)
        user.save()
        rt.is_used = True
        rt.save()
        return Response({"message": "Password reset successfully"})
    except PasswordResetToken.DoesNotExist:
        return Response({"error": "Invalid token"}, status=400)
    except Exception as e:
        logger.error(f"Reset pw error: {e}")
        return Response({"error": "Failed to reset password"}, status=500)


@login_required(login_url='login')
def profile(request):
    user = request.user
    patient_data = Patient.objects.filter(username=user.username).first()
    user_data    = User.objects.filter(username=user.username).first()
    if not patient_data:
        return HttpResponse("Patient data not found", status=404)

    form = CustomUserUpdateForm(initial={
        "firstname":  patient_data.first_name,
        "lastname":   patient_data.last_name,
        "email":      patient_data.email,
        "phone":      patient_data.phone_number,
        "birth_date": patient_data.date_of_birth
    })
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST)
        if form.is_valid():
            patient_data.first_name    = form.cleaned_data["first_name"]
            patient_data.last_name     = form.cleaned_data["last_name"]
            patient_data.email         = form.cleaned_data["email"]
            patient_data.phone_number  = form.cleaned_data["phone"]
            patient_data.date_of_birth = form.cleaned_data["birth_date"]
            user_data.first_name       = form.cleaned_data["first_name"]
            user_data.last_name        = form.cleaned_data["last_name"]
            user_data.email            = form.cleaned_data["email"]
            patient_data.save()
            user_data.save()
            return redirect("profile")
    return render(request, 'users/profile.html', {"form": form})


@login_required(login_url='login')
def cancel_appointment(request, appointment_id):
    appt = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    if request.method == "POST":
        appt.delete()
        return redirect("dashboard")
    return HttpResponse("Method not allowed", status=405)


@never_cache
def privacy_policy(request):
    return render(request, 'users/privacy_policy.html')


@api_view(['GET'])
def search_records(request):
    query = request.GET.get("q", "").lower()
    user_id = 1
    with open("data_mockup/records.json") as f:
        records = json.load(f)
    matched = [
        {k: r[k] for k in r if k != "user_id"}
        for r in records
        if r["user_id"] == user_id and (
            query in r["prescription"].lower() or
            query in r["doctor"].lower()
        )
    ]
    return JsonResponse(matched, safe=False)


@login_required(login_url='login')
def medical_records(request):
    return render(request, 'users/medical_records.html')
