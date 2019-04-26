from django.db import models

class Post(models.Model):
    writer = models.ForeignKey('raycom_users.RaycomCustomUser', on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post_images', default='post_images/default_post_image.png')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('raycom.Tag', related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey('raycom_users.RaycomCustomUser', related_name='user_comments', blank=True, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey('raycom.Post', related_name='post_comments', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('raycom_users.RaycomCustomUser', blank=True, related_name='mylikes')
    dislikes = models.ManyToManyField('raycom_users.RaycomCustomUser', blank=True, related_name='mydislikes')

    def __str__(self):
        return self.text[0:20] + "..."

class Tag(models.Model):
    tag_name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.tag_name
