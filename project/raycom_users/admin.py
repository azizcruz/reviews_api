from django.contrib import admin
from .models import RaycomCustomUser, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class RaycomCustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = RaycomCustomUser

admin.site.register(RaycomCustomUser, RaycomCustomUserAdmin)
admin.site.register(Profile)
