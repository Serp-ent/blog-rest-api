from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Author
from blog.serializers import AuthorSerializer

# Create your views here.
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

