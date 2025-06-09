from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # HTML pages
    path('login/', views.login_page, name="login_page"),
    path('signup/', views.signup_page, name="signup_page"),
    path('signup/provider/', views.signup_provider_page, name="signup_provider_page"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('forgot-password/', views.forgot_password_page, name="forgot_password_page"),
    path('reset-password/', views.reset_password_page, name="reset_password_page"),
    
    # API endpoints
    path('api/login/', views.login, name="login"),
    path('api/register/', views.register, name="register"),
    path('api/register/provider/', views.register_provider, name="register_provider"),
    path('api/logout/', views.logout, name="logout"),
    path('api/validate-token/', views.validate_token, name="validate_token"),
    path('api/forgot-password/', views.forgot_password, name="forgot_password"),
    path('api/reset-password/', views.reset_password, name="reset_password"),
    path('api/validate-reset-token/', views.validate_reset_token, name="validate_reset_token"),
    
    # Root redirect
    path('', lambda request: redirect('login_page')),
]
# Serve media files from MEDIA_ROOT. It will only work when DEBUG=True is set.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)