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
        
        comments = Comment.objects.order_by('-created_at')[:5]
        data['comments'] = CommentSerializer(comments, many=True).data
        return data

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "comments",
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
