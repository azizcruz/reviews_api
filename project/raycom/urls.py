from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

app_name = 'raycom'

router = DefaultRouter()
router.register(r'posts', views.ListPostsView)

urlpatterns = [
    path('', include(router.urls))
]