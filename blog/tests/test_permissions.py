import pytest
from blog import permissions
from blog.models import Blog


@pytest.mark.django_db
def test_blog_owner_has_permissions(author, blog, request_factory):
    # Simulate request from the user_author
    request = request_factory.get("/")
    request.user = author.user

    # Act
    perm = permissions.IsBlogOwner()
    has_perm = perm.has_object_permission(request, None, blog)

    # Assert
    assert has_perm == True


@pytest.mark.django_db
def test_non_owner_dont_have_permissions(other_author, blog, request_factory):
    # Simulate request from the user_author
    request = request_factory.get("/")
    request.user = other_author.user

    # Act
    perm = permissions.IsBlogOwner()
    has_perm = perm.has_object_permission(request, None, blog)

    # Assert
    assert has_perm == False
