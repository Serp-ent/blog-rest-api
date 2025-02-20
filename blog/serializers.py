from rest_framework import serializers
from blog.models import Author, Blog, Comment


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
        fields = ["url", "name", "email", "bio"]


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
            "comments",
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
