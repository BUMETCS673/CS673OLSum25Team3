import pytest
from users.models import Patient
from users.forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserUpdateForm
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
    _ = Patient.objects.create(
        username="test",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        date_of_birth=None,
        phone_number=None
    )
    return sample_user

class TestCustomAuthenticationForm:

    @pytest.mark.django_db
    def test_valid_form(self, user):
        data = {
            "username": user.username,
            "password": "8'V7E5;k"
        }
        form = CustomAuthenticationForm(data=data)
        assert form.is_valid()

    @pytest.mark.django_db
    def test_invalid_form(self, user):
        data = {
            "username": user.username,
            "password": "test123"
        }
        form = CustomAuthenticationForm(data=data)
        assert not form.is_valid()
        data = {
            "username": "test",
            "password": ""
        }
        form = CustomAuthenticationForm(data=data)
        assert not form.is_valid()

class TestCustomUserCreationForm:
    @pytest.mark.django_db
    def test_valid_form(self):
        data = {
            "username": "testuser",
            "password1": "gsid234#$",
            "password2": "gsid234#$",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jane@gmail.com"
        }
        form = CustomUserCreationForm(data=data)
        assert form.is_valid()

    @pytest.mark.parametrize("data", [
        {
            "username": "",
            "password1": "gsid234#$",
            "password2": "gsid234#$",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jane@gmail.com"
        },
        {
            "username": "test",
            "password1": "gsid234#$",
            "password2": "gid234#$",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jane@gmail.com"
        },
        {
            "username": "testuser",
            "password1": "gsid234#$",
            "password2": "gsid234#$",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": ""
        },
        {
            "username": "testuser",
            "password1": "gsid234#$",
            "password2": "gsid234#$",
            "firstname": "",
            "lastname": "Doe",
            "email": "jane@gmail.com"
        },
    ])
    @pytest.mark.django_db
    def test_invalid_form(self, data):
        form = CustomUserCreationForm(data=data)
        assert not form.is_valid()

class TestCustomUserUpdateForm:
    @pytest.mark.django_db
    def test_valid_form(self):
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john@gmail.com",
            "phone": "1234567890",
            "birth_date": "1970-01-01"
        }
        form = CustomUserUpdateForm(data=data)
        assert form.is_valid()

    @pytest.mark.parametrize("data", [
        {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john@gmail.com",
            "phone": "123456789",
            "birth_date": "1970-01-01"
        },
        {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john",
            "phone": "1234567890",
            "birth_date": "1970-01-01"
        },
        {
            "firstname": "",
            "lastname": "",
            "email": "john@gmail.com",
            "phone": "1234567890",
            "birth_date": "1970-01-01"
        }
    ])
    @pytest.mark.django_db
    def test_invalid_form(self, data):
        form = CustomUserUpdateForm(data=data)
        assert not form.is_valid()
        