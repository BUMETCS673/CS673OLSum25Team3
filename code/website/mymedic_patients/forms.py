from django import forms
from .models import Patient


class EditProfileForm(forms.Form):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'pattern': r"[0-9]{10}", 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d'])
    
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