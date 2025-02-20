import pytest
from rest_framework import status
from django.urls import reverse
from blog.models import Blog, Comment


@pytest.mark.django_db
def test_anonymous_user_cannot_create_blog_posts(anon_client):
    # Arrange
    url = reverse("blog-list")
    blog_payload = {"title": "blogTitle", "content": "blogContent,"}
    nblogs_before = Blog.objects.count()

    # Act
    response = anon_client.post(url, blog_payload)

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
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
    assert response.status_code == status.HTTP_403_FORBIDDEN
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