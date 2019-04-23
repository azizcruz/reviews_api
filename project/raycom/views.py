from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import mixins
# Create your views here.


class ListPostsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)