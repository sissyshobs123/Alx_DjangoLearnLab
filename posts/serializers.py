from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at", "comments"]

class LikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(read_only=True)

class EmptySerializer(serializers.Serializer):
    pass