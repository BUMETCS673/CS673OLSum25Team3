from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments_page, name="appointments_page"),
    path('api/appointments/', views.appointments_api, name="appointments_api"),
]

