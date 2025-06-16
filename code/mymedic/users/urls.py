from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # User authentication routes
    path('login/', views.login_page, name='login'),
    path('api/login/', views.login_api, name='api_login'),
    path('logout/', views.logout_page, name='logout'),
    path('api/logout/', views.logout_api, name='api_logout'),

    # Registration routes
    path('register/', views.signup_page, name='register'),
    path('api/register/', views.register, name='api_register'),

    # User dashboard and profile
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

    # Medical records
    path('records/', views.medical_records, name='medical_records'),
    path('api/search/', views.search_records, name='api_search_records'),

    # Appointment management
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),

    # Password management
    path('forgot-password/', views.forgot_password_page, name='forgot_password_page'),
    path('api/forgot-password/', views.forgot_password, name='api_forgot_password'),
    path('reset-password/', views.reset_password_page, name='reset_password_page'),
    path('api/validate-reset-token/', views.validate_reset_token, name='api_validate_reset_token'),
    path('api/reset-password/', views.reset_password, name='api_reset_password'),

    # Privacy policy
    path('privacy/', views.privacy_policy, name='privacy_policy'),

    # Default redirect
    path('', lambda request: redirect('login')),
]
