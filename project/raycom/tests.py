from django.test import TestCase
from .models import (
    Post,
    Tag,
    Comment,
)
from . import views
from rest_framework.test import APIRequestFactory
from .serializers import PostSerializer
# Create your tests here.
class RaycomTests(TestCase):
    def setUp(self):
        # Create a user
        self.user1 = RaycomCustomUser.objects.create(username="aziz", password="gfg1f2gfa")
        self.user2 = RaycomCustomUser.objects.create(username="ali", password="gfg1f2gfa")
        # Create a profile and assign it to user 1
        self.profile1 = Profile.objects.create(user=self.user1)
        # Create two tags
        self.tag1 = Tag.objects.create(tag_name="sport")
        self.tag2 = Tag.objects.create(tag_name="technology")
        # Create a post
        self.post = Post.objects.create(writer=self.user1, title='bla nla', content='sjgjga jsjga sagga')
        # Add the two tags to the post
        self.post.tags.add(self.tag1, self.tag2)
        # Create two comments
        self.comment1 = Comment.objects.create(text='test1', user=self.user1)
        self.comment2 = Comment.objects.create(text='bla bla 2', user=self.user2)
        # Add like to comment 1
        self.comment1.likes.add(self.user1)
        # Add dislike to comment 1
        self.comment1.dislikes.add(self.user2)
        # Add the two comments to the post
        self.post.post_comments.add(self.comment1, self.comment2)
        # Using the standard RequestFactory API to create a form POST request
        self.factory = APIRequestFactory()
        self.view = views.PostsView.as_view({'post': 'post'})


    def test_if_tag_is_created(self):
        self.assertEqual(Tag.objects.all().first().tag_name, 'sport')

    def test_if_post_is_created(self):
        self.assertEqual(Post.objects.all().first().title, 'bla nla')

    def test_if_post_has_comment1(self):
        self.assertEqual(Post.objects.all().first().post_comments.all().first().text, 'test1')
    
    def test_if_post_has_tag(self):
        self.assertEqual(Post.objects.all().first().tags.all().first().tag_name, 'sport')

    def test_if_comment1_has_likes(self):
        self.assertEqual(Post.objects.all().first().post_comments.all().first().likes.all().count(), 1)
    

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