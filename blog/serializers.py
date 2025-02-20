from rest_framework import serializers
from blog.models import Author, Blog, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "email", "bio"]


class BlogSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["author"] = AuthorSerializer(instance.author).data
        return data

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "created_at",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "blog",
            "author",
            "created_at",
            "text",
        ]
