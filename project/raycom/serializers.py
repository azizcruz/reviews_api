from rest_framework import serializers
from .models import (
    Post,
    RaycomCustomUser,
    Comment
)


class RaycomCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaycomCustomUser
        fields = ('username', 'first_name', 'last_name')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('user', 'text', 'likes_count', 'dislikes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()
    def get_dislikes_count(self, obj):
        return obj.dislikes.count()

class PostSerializer(serializers.ModelSerializer):
    writer = RaycomCustomUserSerializer()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['post_image', 'title', 'content', 'writer', 'comments']