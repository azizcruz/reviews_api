from rest_framework import serializers
from .models import RaycomCustomUser, Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Profile
        fields = ('image', 'user', 'first_name', 'last_name', 'rate', 'country')

class RaycomCustomUserSerializerUsersApp(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    # mylikes = serializers.ReadOnlyField(source='mylikes.count')
    # mydislikes = serializers.ReadOnlyField(source='mydislikes.count')
    class Meta:
        depth = 1
        model = RaycomCustomUser
        fields = ('id', 'username', 'profile', 'user_comments', 'mylikes', 'mydislikes')


class RaycomCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaycomCustomUser
        fields = ('username',)

