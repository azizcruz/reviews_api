from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from . import views as posts_views
from raycom_users import views as users_views
from rest_auth.registration.views import VerifyEmailView, RegisterView


app_name = 'raycom'

router = DefaultRouter()
router.register(r'posts', posts_views.PostsView, basename='posts')
router.register(r'users', users_views.UsersView, basename='users')
router.register(r'comments', posts_views.CommentsView, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('raycom-auth/', include('rest_auth.urls')),
    path('raycom-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
     name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
     name='account_confirm_email'),
]