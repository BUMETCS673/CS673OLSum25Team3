from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import PasswordResetToken, PatientProfile, ProviderProfile

@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'created_at', 'is_used', 'is_valid_display']
    list_filter = ['is_used', 'created_at']
    search_fields = ['user__username', 'token']
    readonly_fields = ['token', 'created_at']
    
    def is_valid_display(self, obj):
        return obj.is_valid()
    is_valid_display.boolean = True
    is_valid_display.short_description = 'Is Valid'

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'medical_record_number', 'phone', 'date_of_birth', 'created_at']
    list_filter = ['created_at', 'date_of_birth']
    search_fields = ['user__username', 'user__email', 'medical_record_number', 'phone']
    readonly_fields = ['medical_record_number', 'created_at', 'updated_at']

@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'license_number', 'specialization', 'clinic_name', 'phone']
    list_filter = ['specialization', 'clinic_name']
    search_fields = ['user__username', 'license_number', 'clinic_name']
    readonly_fields = ['created_at', 'updated_at']

# Customize the default User admin
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_login']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering = ['-date_joined']
