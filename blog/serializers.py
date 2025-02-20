from rest_framework import serializers
from blog.models import Author, Blog, Comment
from django.contrib.auth.models import User


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, instance):
        from .serializers import CommentSerializer

        request = self.context.get("request")

        data = super().to_representation(instance)
        comments = instance.comments.order_by("-created_at")[:5]
        data["comments"] = CommentSerializer(
            comments, many=True, context={"request": request}
        ).data

        return data

    class Meta:
        model = Author
        fields = ["url", "bio"]


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        request = self.context.get("request")

        data = super().to_representation(instance)

        data["author"] = AuthorSerializer(
            instance.author, context={"request": request}
        ).data

        comments = instance.comments.order_by("-created_at")[:5]
        data["comments"] = CommentSerializer(
            comments, many=True, context={"request": request}
        ).data
        return data

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "created_at",
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "url",
            "blog",
            "author",
            "created_at",
            "text",
        ]
        read_only_fields = ["author", "created_at"]

    def update(self, instance, validated_data):
        # Prevent updating the blog field
        validated_data.pop("blog", None)
        return super().update(instance, validated_data)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
        )
        return user
