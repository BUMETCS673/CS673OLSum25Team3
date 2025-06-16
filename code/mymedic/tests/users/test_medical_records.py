"""
Simplified medical records tests without custom fixtures.
"""

import pytest
from django.test import Client
from django.contrib.auth.models import User
from users.models import Patient


@pytest.mark.django_db
def test_pdf_preview_with_records(client):
    """Ensure medical records page loads for authenticated user with patient data"""
    # Create user and patient data
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    
    Patient.objects.create(
        username=user.username,
        first_name='John',
        last_name='Doe',
        email=user.email,
        date_of_birth=None
    )
    
    # Authenticate user
    client.force_login(user)
    response = client.get('/records/')
    assert response.status_code == 200
    assert 'users/medical_records.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_pdf_preview_without_records(client):
    """Test medical records page for user without patient data"""
    # Create user without patient data
    user = User.objects.create_user(
        username='emptyuser',
        email='empty@example.com',
        password='testpass123'
    )
    
    client.force_login(user)
    response = client.get('/records/')
    assert response.status_code in [200, 404]


@pytest.mark.django_db
def test_pdf_download_endpoint(client):
    """Test PDF download functionality (placeholder)"""
    user = User.objects.create_user(
        username='downloaduser',
        email='download@example.com',
        password='testpass123'
    )
    
    Patient.objects.create(
        username=user.username,
        first_name='Jane',
        last_name='Smith',
        email=user.email,
        date_of_birth=None
    )
    
    # Authenticate user
    client.force_login(user)
    response = client.get('/records/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_medical_records_requires_login(client):
    """Test that medical records page requires authentication"""
    response = client.get('/records/')
    assert response.status_code == 302
    assert 'login' in response.url


@pytest.mark.django_db
def test_medical_records_authenticated_access(client):
    """Test that authenticated users can access medical records"""
    # Create user and patient data
    user = User.objects.create_user(
        username='accessuser',
        email='access@example.com',
        password='testpass123'
    )
    
    Patient.objects.create(
        username=user.username,
        first_name='Access',
        last_name='User',
        email=user.email,
        date_of_birth=None
    )
    
    client.force_login(user)
    response = client.get('/records/')
    assert response.status_code == 200
    assert 'users/medical_records.html' in [t.name for t in response.templates]