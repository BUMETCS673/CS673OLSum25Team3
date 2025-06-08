from django import forms
from .models import Patient


class EditProfileForm(forms.Form):
    class Meta:
        model = Patient

    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}))
    
    def clean(self):
        return super().clean()
    
    def save(self, user):
        # Update patient profile if it exists
        try:
            patient = user.patients.first()
            if patient:
                patient.first_name = self.cleaned_data.get('first_name', patient.first_name)
                patient.last_name = self.cleaned_data.get('last_name', patient.last_name)
                patient.email = self.cleaned_data.get('email', patient.email)
                patient.phone_number = self.cleaned_data.get('phone_number', patient.phone_number)
                patient.date_of_birth = self.cleaned_data.get('date_of_birth', patient.date_of_birth)
                patient.save()
        except Patient.DoesNotExist:
            pass