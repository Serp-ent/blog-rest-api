from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Author, Blog, Comment
from blog.serializers import AuthorSerializer, BlogSerializer, CommentSerializer


# Create your views here.
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
