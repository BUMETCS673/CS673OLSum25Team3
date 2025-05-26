from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page),
    path('signup/', views.signup_page),
    path('api/login/', views.login),
    path('api/register/', views.register),
    path("dashboard/", views.dashboard),
    path('', lambda request: redirect('/login/')), 
]

# Serve media files from MEDIA_ROOT. It will only work when DEBUG=True is set.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
