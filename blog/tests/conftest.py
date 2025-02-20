import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture()
@pytest.mark.django_db
def user():
    return User.objects.create_user("testuser", "password")


@pytest.fixture
def anon_client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user=user)

    return client
