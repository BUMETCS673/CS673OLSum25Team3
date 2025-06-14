"""URL Patterns for user features which get imported into the main urls module"""
from django.urls import path
from . import views
from .views import mfa_verify
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('mlogin', views.mlogin, name='mlogin'),
    path('profile', views.profile, name='profile'),
    path('mlogout', views.mlogout, name='mlogout'),
    path('', views.mlogin, name=''),  # Default route to login
    path('mfa/', mfa_verify, name='mfa_verify'),
]