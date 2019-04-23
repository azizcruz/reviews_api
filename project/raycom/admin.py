from django.contrib import admin
from .models import (
    RaycomCustomUser,
    Post,
    Comment,
    Tag,
    Profile
)

admin.site.register(Profile)
admin.site.register(RaycomCustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
