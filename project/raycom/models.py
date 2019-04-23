from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator

class RaycomCustomUser(AbstractUser):
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Raycom Custom User'

class Profile(models.Model):
    user = models.OneToOneField('raycom.RaycomCustomUser', related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images", default="profile_images/default_profile_image.png")
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    rate = models.IntegerField(default=0, validators=[MaxLengthValidator(5), MinLengthValidator(0)])
    country = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.user


class Post(models.Model):
    writer = models.ForeignKey('raycom.RaycomCustomUser', on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post_images', default='post_images/default_post_image.png')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('raycom.Tag', related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey('raycom.RaycomCustomUser', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('raycom.Post', related_name='comments', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('raycom.RaycomCustomUser', blank=True, related_name='mylikes')
    dislikes = models.ManyToManyField('raycom.RaycomCustomUser', blank=True, related_name='mydislikes')

    def __str__(self):
        return self.text[0:20] + "..."

class Tag(models.Model):
    tag_name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.tag_name
