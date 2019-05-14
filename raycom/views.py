from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, CommentSerializerRaycom
from .models import Post, Comment
from rest_framework import mixins
from .mixins import CustomUpdateModelMixin
from rest_framework import permissions
# Create your views here.


class PostsView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentsView(mixins.CreateModelMixin, mixins.ListModelMixin, CustomUpdateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerRaycom
    lookup_field = "pk"

    