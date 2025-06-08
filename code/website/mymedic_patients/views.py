from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import EditProfileForm
from django.http import HttpResponse
from .models import Patient
from django.contrib.auth.models import AnonymousUser
# Create your views here.

def edit_profile(request):
    token = request.headers.get('Authorization')
    if not token:
        return HttpResponse("Unauthorized", status=401)
    
    user = request.user
    if isinstance(user, AnonymousUser) or not user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    
    patient_data = Patient.objects.filter(user=user).first()
    initial_data = {
        'first_name': patient_data.first_name,
        'last_name': patient_data.last_name,
        'email': patient_data.email,
        'phone_number': patient_data.phone_number,
        'date_of_birth': patient_data.date_of_birth,
    }
    return render(request, "edit_profile.html", {"form": EditProfileForm(initial=initial_data)})
    
@api_view(['POST'])
def submit_edits(request):
    token = request.headers.get('Authorization')
    if not token:
        return HttpResponse("Unauthorized", status=401)
    user = request.user
    if isinstance(user, AnonymousUser) or not user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    
    patent_data = Patient.objects.filter(user=user).first()
    if not patent_data:
        return HttpResponse("Patient data not found", status=404)
    
    first_name = request.data.get('first_name', patent_data.first_name)
    last_name = request.data.get('last_name', patent_data.last_name)
    email = request.data.get('email', patent_data.email)
    phone = request.data.get('phone', patent_data.phone_number)
    birthdate = request.data.get('birthdate', patent_data.date_of_birth)
    patent_data.first_name = first_name
    patent_data.last_name = last_name
    patent_data.email = email
    patent_data.phone_number = phone
    patent_data.date_of_birth = birthdate
    try:
        patent_data.save()
    except Exception as e:
        return HttpResponse(f"Error updating profile: {str(e)}", status=500)
    return HttpResponse("Profile updated successfully.")