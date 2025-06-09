from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page, name="login_page"),
    path('signup/', views.signup_page, name="signup_page"),
    path('api/login/', views.login, name="login"),
    path('api/register/', views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('api/appointments/', views.appointments_view,
         name="appointments_view"),
    path('', lambda request: redirect('/login/')),
]

# Serve media files from MEDIA_ROOT. It will only work when DEBUG=True is set.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
