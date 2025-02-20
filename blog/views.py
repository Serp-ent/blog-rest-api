from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Author, Blog, Comment
from blog.serializers import AuthorSerializer, BlogSerializer, CommentSerializer
from rest_framework import permissions


# Create your views here.
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=user.author)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
