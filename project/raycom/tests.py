from django.test import TestCase
from .models import (
    Post,
    Tag,
    Comment,
)
from . import views
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from .serializers import PostSerializer
from raycom_users.models import RaycomCustomUser, Profile
# Create your tests here.
class RaycomTests(TestCase):
    def setUp(self):
        # Create a user
        self.user1 = RaycomCustomUser.objects.create(username="aziz", password="gfg1f2gfa")
        self.user2 = RaycomCustomUser.objects.create(username="ali", password="gfg1f2gfa")
        self.comment1 = Comment.objects.create(text='test1', user=self.user1)
        self.comment2 = Comment.objects.create(text='bla bla 2', user=self.user2)
        # Using the standard RequestFactory API to create a form POST request
        self.factory = APIRequestFactory()
        self.view = views.PostsView.as_view({'post': 'post'})
        self.client = APIClient()

    def test_adding_like(self):
        data = {
            "user_id": self.user1.id,
            "action": "like"
        }
        response = self.client.patch(f'http://localhost:8000/comments/{self.comment1.id}/', data)

        import pdb; pdb.set_trace()
    

    # Views Testing
    def test_creating_a_post_(self):
        data = {
                "post_image": "",
                "title": "test_create_post_title",
                "content": "test_create_post_content"
            }
        request = self.factory.post('/posts/', data)
        request.user = self.user1
        response = self.view(request)
        self.assertAlmostEqual(response.status_code, 201)