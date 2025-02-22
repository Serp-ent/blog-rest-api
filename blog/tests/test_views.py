import pytest
from rest_framework import status
from django.urls import reverse
from blog.models import Blog, Comment
from blog.views import BlogViewset


@pytest.mark.django_db
def test_anonymous_user_cannot_create_blog_posts(anon_client):
    # Arrange
    url = reverse("blog-list")
    blog_payload = {"title": "blogTitle", "content": "blogContent,"}
    nblogs_before = Blog.objects.count()

    # Act
    response = anon_client.post(url, blog_payload)

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Blog.objects.count() == nblogs_before

@pytest.mark.django_db
def test_authenticated_user_created_blog_posts(auth_client):
    # Arrange
    url = reverse("blog-list")
    blog_payload = {"title": "blogTitle", "content": "blogContent,"}
    nblogs_before = Blog.objects.count()

    # Act
    response = auth_client.post(url, blog_payload)

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Blog.objects.count() == nblogs_before + 1


@pytest.mark.django_db
def test_anonymous_user_cannot_create_comment(anon_client, blog):
    # Arrange
    url = reverse("comment-list")
    blog_url = reverse('blog-detail', kwargs={'pk': blog.id})
    comment_payload = {"blog": blog_url, "text": "blogContent,"}
    ncomments_before = Comment.objects.count()

    # Act
    response = anon_client.post(url, comment_payload)

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Comment.objects.count() == ncomments_before

@pytest.mark.django_db
def test_authenticated_user_created_comment(auth_client, blog):
    # Arrange
    url = reverse("comment-list")
    blog_url = reverse('blog-detail', kwargs={'pk': blog.id})
    comment_payload = {"blog": blog_url, "text": "blogContent,"}
    ncomments_before = Comment.objects.count()

    # Act
    response = auth_client.post(url, comment_payload)

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Comment.objects.count() == ncomments_before + 1

@pytest.mark.django_db
def test_publish_blog_as_owner(auth_client, author, blog):
    url = reverse('blog-publish', kwargs={'pk': blog.id})

    response = auth_client.post(url)

    blog.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert blog.is_published == True, "The blog post was not published"


@pytest.mark.django_db
def test_publish_blog_as_anon(anon_client, blog):
    url = reverse('blog-publish', kwargs={'pk': blog.id})

    response = anon_client.post(url)

    blog.refresh_from_db()
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert blog.is_published == False, "The blog post was published"


@pytest.mark.django_db
def test_publish_blog_as_non_owner(auth_client, other_author, blog):
    url = reverse('blog-publish', kwargs={'pk': blog.id})
    auth_client.force_authenticate(user=other_author.user)

    response = auth_client.post(url)

    blog.refresh_from_db()
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert blog.is_published == False, "The blog post was published"



