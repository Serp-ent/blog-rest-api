import pytest
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from blog.models import Blog
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


@pytest.fixture()
@pytest.mark.django_db
def author(user):
    return user.author


@pytest.fixture
@pytest.mark.django_db
def blog(author):
    return Blog.objects.create(author=author, title="title", content="content")


@pytest.fixture()
@pytest.mark.django_db
def other_author():
    user = User.objects.create_user(username="otherAuthor")
    return user.author


@pytest.fixture()
def request_factory():
    return APIRequestFactory()
