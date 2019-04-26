from django.test import TestCase
from .models import RaycomCustomUser, Profile
from . import views
from rest_framework.test import APIRequestFactory
from .serializers import PostSerializer


class RaycomTests(TestCase):
    def setUp(self):
        # Create a user
        self.user1 = RaycomCustomUser.objects.create(username="aziz", password="gfg1f2gfa")
        self.user2 = RaycomCustomUser.objects.create(username="ali", password="gfg1f2gfa")
        # Create a profile and assign it to user 1
        self.profile1 = Profile.objects.create(user=self.user1)


    def test_if_user_is_created(self):        
        self.assertEqual(RaycomCustomUser.objects.all().first().username, 'aziz')