import pytest
from django.contrib.auth.models import User
from blog.models import Blog, Author


@pytest.mark.django_db
@pytest.mark.parametrize(
    "username,is_admin",
    [
        ("testuser", False),
        ("ash", False),
        ("admin", True),
        ("admin2", True),
    ],
    ids=["casual User 1", "casual User 2", "superuser 1", "superuser 2"],
)
def test_author_model_created_on_user_creation(username, is_admin):
    # Act
    if is_admin:
        create_user = User.objects.create_superuser
    else:
        create_user = User.objects.create_user

    user = create_user(username=username)

    # Assert
    assert (
        getattr(user, "author", None) is not None
    ), f"Author model was not created on {'Superuser' if is_admin else 'Casual User'} creation"
    author = Author.objects.filter(user=user).get()
    assert author.user == user
