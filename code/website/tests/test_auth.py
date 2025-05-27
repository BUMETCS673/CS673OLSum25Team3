import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

# User fixture 
@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username="alice", password="secret123")

# Test: Dashboard (HTML) 
@pytest.mark.django_db
def test_dashboard_returns_html(client, user):
    client.login(username=user.username, password="secret123")
    resp = client.get(reverse("dashboard"))

    assert resp.status_code == 200
    assert "text/html" in resp.headers.get("Content-Type", "").lower()
    assert b"Dashboard" in resp.content or b"Welcome" in resp.content

# Parametrized: Public Pages 
@pytest.mark.django_db
@pytest.mark.parametrize("url_name, expected_text", [
    ("login_page", b"Login"),
    ("signup_page", b"Sign Up"),
])
def test_public_pages_load(client, url_name, expected_text):
    resp = client.get(reverse(url_name))
    assert resp.status_code == 200
    assert expected_text in resp.content

# Test: Login with wrong credentials 
@pytest.mark.django_db
def test_login_fails_with_invalid_credentials(client):
    resp = client.post(
        reverse("login"),
        {"username": "fakeuser", "password": "wrongpass"},
        content_type="application/json"
    )
    assert resp.status_code == 401 or resp.status_code == 400

# Test: Signup flow (happy path)
@pytest.mark.django_db
def test_user_can_register(client):
    resp = client.post(
        reverse("register"),
        {"username": "newuser", "password": "newpass123"},
        content_type="application/json"
    )
    assert resp.status_code == 201 or resp.status_code == 200
    body = resp.json()
    assert "message" in body or "success" in body

# Test: Login after signup 
@pytest.mark.django_db
def test_user_can_login_after_register(client):
    # Register new user
    client.post(
        reverse("register"),
        {"username": "testuser", "password": "abc12345"},
        content_type="application/json"
    )

    # Now login
    login_resp = client.post(
        reverse("login"),
        {"username": "testuser", "password": "abc12345"},
        content_type="application/json"
    )
    data = login_resp.json()
    assert login_resp.status_code == 200
    assert "access" in data or "token" in data
