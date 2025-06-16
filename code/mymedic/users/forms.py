"""
This module holds the form definition and styles them

@ai-generated
Tool: GitHub Copilot
Prompt: N/A (Code completion unprompted)
Generated on: 06-08-2025
Modified by: Tyler Gonsalves
Modifications: Added CSS styling and updated docstrings
Verified: ✅ Unit tested, reviewed
"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import RegexValidator
from django.forms.widgets import PasswordInput, TextInput, EmailInput, DateInput
class CustomUserCreationForm(UserCreationForm):
    """
    Custom form for user registration.
    Inherits from Django's UserCreationForm.
    """
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom form for user authentication.
    Inherits from Django's AuthenticationForm.
    """
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class CustomUserUpdateForm(forms.Form):
    """
    Custom form for updating user information.
    Inherits from Django's ModelForm.
    """
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(widget=TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
                            validators=[RegexValidator(regex=r'^\d{10}$', message='Phone number must be 10 digits.')])
    birth_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
                                 validators=[RegexValidator(regex=r'^\d{4}-\d{2}-\d{2}$')])
