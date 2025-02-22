from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from blog.permissions import IsBlogOwner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from blog.models import Author, Blog, Comment
from rest_framework.views import APIView
from blog.serializers import (
    AuthorSerializer,
    BlogSerializer,
    CommentSerializer,
    UserRegistrationSerializer,
)
from rest_framework import permissions


# Create your views here.
class AuthorViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# TODO: add filtering by title/author
# TODO: generate OpenAPI/Swagger documentation
# TODO: implement versioned API (v1/v2)
class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=user.author)

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[permissions.IsAuthenticated, IsBlogOwner],
    )
    def publish(self, request, pk=None):
        blog: Blog = self.get_object()
        blog.is_published = True
        blog.save()

        serializer = self.get_serializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def comments(self, request: Request, pk=None):
        blog_post = self.get_object()
        comments = Comment.objects.filter(blog=blog_post)
        serializer = CommentSerializer(
            comments, many=True, context={"request": request}
        )

        return Response(serializer.data)


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
        content = {"message": "Hello! You're authenticated using JWT"}
        return Response(content)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
