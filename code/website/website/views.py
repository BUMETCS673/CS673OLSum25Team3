import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# HTML pages
def login_page(request):
    return render(request, "login.html")

def signup_page(request):
    return render(request, "signup.html")

def dashboard(request):
    return render(request, "dashboard.html")


# REST API endpoints
@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)
    User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully"})

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })
    return Response({"error": "Invalid credentials"}, status=400)

"""
@ai-generated
Tool: ChatGPT (OpenAI)
Prompt: "Write a Django search API view that filters JSON medical records by doctor or prescription for a specific user"
Generated on: 2025-06-07
Modified by: Mengliang Tan
Modifications: Add fake id for testing
Reason for using JSON:
The team has not yet set up a real database, so this view uses a local `records.json` file as a temporary data source. This allows 
frontend development and testing to proceed while backend models and database configurations are still in progress.

Verified: ✅ Tested via frontend
"""
@api_view(['GET'])
def search(request):
    query = request.GET.get("q", "").lower()
    user_id = 1  # fake id for testing

    with open("data_mockup/records.json") as f:
        records = json.load(f)

    matched = [
        {key: r[key] for key in r if key != "user_id"}
        for r in records
        if r["user_id"] == user_id and (
            query in r["prescription"].lower() or query in r["doctor"].lower()
        )
    ]

    return JsonResponse(matched, safe=False)

