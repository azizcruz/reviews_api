from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views as posts_views
from raycom_users import views as users_views

app_name = 'raycom'

router = DefaultRouter()
router.register(r'posts', posts_views.PostsView, basename='posts')
router.register(r'users', users_views.UsersView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('raycom-auth/', include('rest_auth.urls')),
    path('raycom-auth/registration/', include('rest_auth.registration.urls'))
]