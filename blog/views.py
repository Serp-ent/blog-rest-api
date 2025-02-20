from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import generics
from blog.models import Author, Blog, Comment
from rest_framework.views import APIView
from blog.serializers import AuthorSerializer, BlogSerializer, CommentSerializer, UserRegistrationSerializer
from rest_framework import permissions


# Create your views here.
class AuthorViewset(viewsets.ReadOnlyModelViewSet):
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=user.author)


class AuthTestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        content = {'message': "Hello! You're authenticated using JWT"}
        return Response(content)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
