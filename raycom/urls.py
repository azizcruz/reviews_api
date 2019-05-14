from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from . import views as posts_views



router = DefaultRouter()
router.register(r'posts', posts_views.PostsView, basename='posts')
router.register(r'comments', posts_views.CommentsView, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
     
]