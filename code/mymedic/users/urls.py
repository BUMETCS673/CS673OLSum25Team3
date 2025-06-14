"""URL Patterns for user features which get imported into the main urls module"""
from django.urls import path
from . import views
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('mlogin', views.mlogin, name='mlogin'),
    path('profile', views.profile, name='profile'),
    path('mlogout', views.mlogout, name='mlogout'),
    path('', views.mlogin, name=''),  # Default route to login
    path("privacy/", views.privacy_policy, name="privacy_policy"),
    
]