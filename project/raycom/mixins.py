from raycom_users.models import RaycomCustomUser
from .models import Comment
from rest_framework.exceptions import NotFound, NotAcceptable


class CustomUpdateModelMixin(object):

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if 'action' in request.data and 'user_id' in request.data:
            # Assign action variable and get user
            action = request.data['action']

            try:
                user = RaycomCustomUser.objects.get(id=request.data['user_id'])
            except RaycomCustomUser.DoesNotExist:
                raise NotFound('User was not found.')

            # Check if user has a like if yes remove his dislike and add his like
            if action == 'like': 
                if user.id in request.data.get('dislikes'):
                    request.data.get('dislikes').remove(user.id)
                if user.id not in request.data.get('likes'):
                    request.data.get('likes').append(user.id)

            # Check if user has a dislike if yes remove his like and add his dislike
            elif action == 'dislike': 
                if user.id in request.data.get('likes'):
                    request.data.get('likes').remove(user.id)
                if user.id not in request.data.get('dislikes'):
                    request.data.get('dislikes').append(user.id)
            
            else:
                raise NotAcceptable('Please specify which action like or dislike')

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        