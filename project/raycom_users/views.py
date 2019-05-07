from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, views
from .serializers import RaycomCustomUserSerializerUsersApp
from .models import RaycomCustomUser
from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import SessionAuthentication
class UsersView(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = RaycomCustomUser.objects.all()
    serializer_class = RaycomCustomUserSerializerUsersApp

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)