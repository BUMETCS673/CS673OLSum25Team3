"""URL Patterns for user-related views in the MyMedic app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mlogin, name='root'),  # Default route to login page
    path('mlogin', views.mlogin, name='mlogin'),
    path('mlogout', views.mlogout, name='mlogout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('records/', views.medical_records, name='medical_records'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path("privacy/", views.privacy_policy, name="privacy_policy"),
    path('api/search/', views.search_records, name='search'),
]


