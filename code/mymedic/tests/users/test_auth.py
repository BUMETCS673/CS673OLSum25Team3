"""Unit tests for user creation and authentication"""
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

@pytest.fixture
def user(db):
    User = get_user_model()
    sample_user = User.objects.create_user(
        username="test",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="8'V7E5;k"
    )
    return sample_user

@pytest.mark.django_db
@pytest.mark.parametrize("url_name", [
    ("login"),
    ("register"),
])
def test_public_pages(client, url_name):
    resp = client.get(reverse(url_name))
    assert resp.status_code == 200

@pytest.mark.django_db
def test_login(client, user):
    logged_in = client.login(username=user.username, password="8'V7E5;k")
    assert logged_in

@pytest.mark.django_db
def test_bad_login(client, user):
    logged_in = client.login(username="notauser", password="sample")
    assert not logged_in
    logged_in = client.login(username=user.username, password="sample")
    assert not logged_in