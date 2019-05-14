from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class RaycomCustomUser(AbstractUser):
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Raycom Custom User'

class Profile(models.Model):
    user = models.OneToOneField('raycom_users.RaycomCustomUser', related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images", default="profile_images/default_profile_image.png")
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    rate = models.IntegerField(default=0, validators=[MaxValueValidator(5, 'Value should be between 0 and 5'), MinValueValidator(0, 'Value should be between 0 and 5')])
    country = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Create a new profile when a user is created and give this profile the user that was created.
@receiver(post_save, sender=RaycomCustomUser)
def create_raycom_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save the new created profile.
@receiver(post_save, sender=RaycomCustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()