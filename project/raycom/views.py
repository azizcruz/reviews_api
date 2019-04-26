from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
# Create your views here.


class PostsView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)