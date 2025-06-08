from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework_simplejwt.backends import TokenBackend
from .models import Patient
from django.http import HttpResponse
# Create your views here.
def edit_profile(request):
    print("Edit profile view accessed")
    token = request.GET.get('token', None)
    print(f"Token received: {token}")
    patient_data = Patient.objects.all()[0]
    user = patient_data.user if patient_data else None
    return render(request, "edit_profile.html", {"user": user, "patient": patient_data})
    # if not token:
    #     print("No token provided")
    # try:
    #     # Validate the token
    #     token_backend = TokenBackend(algorithm='HS256')
    #     validated_token = token_backend.decode(token, verify=True)
    #     user = validated_token.get('user')
    #     if not user:
    #         print("Invalid token or user not found")
    #         return HttpResponse("Invalid token or user not found", status=401)
    #     else:
    #         # Here you can fetch user details and pass them to the template
    #         # For example, you might want to fetch the user's profile information
    #         # and render it in the edit profile page.
    #         patient_data = Patient.objects.filter(user=user).first()
    #         if not patient_data:
    #             print("No patient data found for user")
    #             return HttpResponse("No patient data found for user", status=404)
    #         else:
    #             print(f"Patient data found: {patient_data}")
    #         return render(request, "edit_profile.html", {"user": user, "patient": patient_data})
    # except Exception as e:
    #     # Handle token validation errors
    #     print(f"Token validation error: {e}")
    #     return HttpResponse("Invalid token", status=401)
    
@api_view(['POST'])
def submit_edits(request):
    pass