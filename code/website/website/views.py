from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import never_cache
from .models import PasswordResetToken, PatientProfile, ProviderProfile
import logging
from datetime import datetime
from django.utils import timezone

logger = logging.getLogger(__name__)

# ─── HTML PAGES ────────────────────────────────────────────────────────────────

@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "login.html")

@never_cache
def signup_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "signup.html")

@never_cache
def signup_provider_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "signup_provider.html")

@never_cache
def dashboard(request):
    token = request.COOKIES.get('access_token') or request.session.get('access_token')
    if not token:
        return redirect('login_page')
    try:
        jwt_auth       = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(token)
        user            = jwt_auth.get_user(validated_token)
        return render(request, "dashboard.html", {'user': user})
    except (InvalidToken, TokenError):
        return redirect('login_page')

@never_cache
def forgot_password_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "forgot_password.html")

@never_cache
def reset_password_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    token = request.GET.get('token')
    return render(request, "reset_password.html", {'token': token})


# ─── API ENDPOINTS ─────────────────────────────────────────────────────────────

@api_view(['POST'])
def register(request):
    # Required fields
    username   = request.data.get("username")
    password   = request.data.get("password")
    email      = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name  = request.data.get("last_name")
    # Optional
    phone         = request.data.get("phone", "")
    date_of_birth = request.data.get("date_of_birth", None)

    # Validation
    if not all([username, password, email, first_name, last_name]):
        return Response({"error": "Please provide all required fields"}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already registered"}, status=400)

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        dob_date = None
        if date_of_birth and date_of_birth.strip():
            try:
                dob_date = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            except ValueError:
                logger.warning(f"Invalid date format for date_of_birth: {date_of_birth}")

        PatientProfile.objects.create(
            user=user,
            phone=phone or "",
            date_of_birth=dob_date
        )

        if user.email:
            send_mail(
                'Welcome to MyMedic',
                f'Hi {first_name},\n\nThank you for registering with MyMedic!\n\nUsername: {username}\n\nBest regards,\nMyMedic Team',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,
            )

        return Response({"message": "Account created successfully!"})

    except Exception as e:
        if 'user' in locals():
            user.delete()
        logger.error(f"Registration error: {e}")
        return Response({"error": f"Failed to create account: {str(e)}"}, status=500)


@api_view(['POST'])
def register_provider(request):
    # Required user fields
    username   = request.data.get("username")
    password   = request.data.get("password")
    email      = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name  = request.data.get("last_name")
    # Provider-specific
    license_number = request.data.get("license_number")
    specialization = request.data.get("specialization")
    clinic_name    = request.data.get("clinic_name")
    clinic_address = request.data.get("clinic_address")
    phone          = request.data.get("phone", "")

    # Validation
    if not all([username, password, email, first_name, last_name,
                license_number, specialization, clinic_name, clinic_address]):
        return Response({"error": "Please provide all required fields"}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already registered"}, status=400)
    if ProviderProfile.objects.filter(license_number=license_number).exists():
        return Response({"error": "License number already in use"}, status=400)

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        ProviderProfile.objects.create(
            user=user,
            license_number=license_number,
            specialization=specialization,
            clinic_name=clinic_name,
            clinic_address=clinic_address,
            phone=phone
        )

        # Welcome email for providers
        if user.email:
            send_mail(
                'Welcome to MyMedic as a Provider',
                f'Hello {first_name},\n\nYour provider account has been created successfully!\n\nUsername: {username}\n\nBest regards,\nMyMedic Team',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,
            )

        return Response({"message": "Provider account created successfully!"})

    except Exception as e:
        if 'user' in locals():
            user.delete()
        logger.error(f"Provider registration error: {e}")
        return Response({"error": f"Failed to create provider account: {str(e)}"}, status=500)


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user     = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        response = Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "full_name": f"{user.first_name} {user.last_name}"
        })
        request.session['access_token'] = str(refresh.access_token)
        return response

    return Response({"error": "Invalid credentials"}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_token(request):
    user = request.user
    is_provider = hasattr(user, 'provider_profile')
    return Response({
        "valid": True,
        "username": user.username,
        "full_name": f"{user.first_name} {user.last_name}",
        "role": "provider" if is_provider else "patient"
    })


@api_view(['POST'])
def logout(request):
    request.session.flush()
    return Response({"message": "Logged out successfully"})


@api_view(['POST'])
def forgot_password(request):
    username_or_email = request.data.get("username")
    if not username_or_email:
        return Response({"error": "Please provide username or email"}, status=400)

    try:
        if '@' in username_or_email:
            user = User.objects.get(email=username_or_email)
        else:
            user = User.objects.get(username=username_or_email)

        reset_token = PasswordResetToken.objects.create(user=user)
        reset_url   = request.build_absolute_uri(f'/reset-password/?token={reset_token.token}')

        if user.email:
            send_mail(
                'Password Reset Request - MyMedic',
                f'Hello {user.first_name},\n\nYou requested a password reset. Click here:\n{reset_url}\n\nExpires in 1 hour.\n\nMyMedic Team',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return Response({"message": f"Password reset link sent to {user.email[:3]}***{user.email[-10:]}"})
        else:
            return Response({"error": "No email on file"}, status=400)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    except Exception as e:
        logger.error(f"Forgot password error: {e}")
        return Response({"error": "Failed to send reset email"}, status=500)


@api_view(['POST'])
def reset_password(request):
    token       = request.data.get("token")
    new_password = request.data.get("new_password")

    try:
        reset_token = PasswordResetToken.objects.get(token=token)
        if not reset_token.is_valid():
            return Response({"error": "Invalid or expired token"}, status=400)

        user = reset_token.user
        user.set_password(new_password)
        user.save()

        reset_token.is_used = True
        reset_token.save()

        return Response({"message": "Password reset successfully"})

    except PasswordResetToken.DoesNotExist:
        return Response({"error": "Invalid token"}, status=400)
    except Exception as e:
        logger.error(f"Reset password error: {e}")
        return Response({"error": "Failed to reset password"}, status=500)


@api_view(['POST'])
def validate_reset_token(request):
    token = request.data.get("token")
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
        if reset_token.is_valid():
            return Response({"valid": True, "username": reset_token.user.username})
        else:
            return Response({"valid": False, "error": "Token expired or used"}, status=400)
    except PasswordResetToken.DoesNotExist:
        return Response({"valid": False, "error": "Invalid token"}, status=400)
