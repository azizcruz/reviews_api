from django.test import TestCase
from .models import (
    Post,
    RaycomCustomUser,
    Tag,
    Comment
)
from .serializers import PostSerializer
# Create your tests here.
class RaycomTests(TestCase):
    def setUp(self):
        # Create a user
        self.user1 = RaycomCustomUser.objects.create(username="aziz", password="gfg1f2gfa")
        self.user2 = RaycomCustomUser.objects.create(username="ali", password="gfg1f2gfa")
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
        self.post.comments.add(self.comment1, self.comment2)

    def test_if_user_is_created(self):
        import pdb; pdb.set_trace()
        
        self.assertEqual(RaycomCustomUser.objects.all().first().username, 'aziz')

    def test_if_tag_is_created(self):
        self.assertEqual(Tag.objects.all().first().tag_name, 'sport')

    def test_if_post_is_created(self):
        self.assertEqual(Post.objects.all().first().title, 'bla nla')

    def test_if_post_has_comment1(self):
        self.assertEqual(Post.objects.all().first().comments.all().first().text, 'test1')
    
    def test_if_post_has_tag(self):
        self.assertEqual(Post.objects.all().first().tags.all().first().tag_name, 'sport')

    def test_if_comment1_has_likes(self):
        self.assertEqual(Post.objects.all().first().comments.all().first().likes.all().count(), 1)