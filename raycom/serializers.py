from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from .models import (
    Post,
    Comment
)

from raycom_users.serializers import RaycomCustomUserSerializer

class CommentSerializerRaycom(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'likes', 'dislikes', 'post', 'user']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('user', 'text', 'likes_count', 'dislikes_count')

    # Resturn likes and dislikes as counted numbers instead of lists.
    def get_likes_count(self, obj):
        return obj.likes.count()
    def get_dislikes_count(self, obj):
        return obj.dislikes.count()
        
class PostSerializer(serializers.ModelSerializer):
    writer = RaycomCustomUserSerializer(read_only=True)
    post_comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['post_image', 'title', 'content', 'writer', 'post_comments']

    # Add the post writer explicitly.
    def create(self, validated_data):
        if self.context['request'].user.username is not '':
            user = self.context['request'].user
            post = Post(writer=user, **validated_data)
            post.save()
            return post
        else:
            raise NotAuthenticated('You need to be logged in to perform this action.')
    