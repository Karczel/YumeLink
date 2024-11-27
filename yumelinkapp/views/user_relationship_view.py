from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from yumelinkapp.models import User, Block, Follow


class UserRelationShipView(LoginRequiredMixin, ListView):
    template_name = 'yumelink/user_relationship.html'
    context_object_name = 'relationships'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj_type = self.request.GET.get('type', '')
        context['obj_type'] = obj_type
        context['user'] = User.objects.get(id=self.request.user.id)
        context['viewed_user'] = self.get_viewed_user()
        return context

    def get_viewed_user(self):
        """Fetch the user being viewed by username."""
        username = self.kwargs.get('username')
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(self.request, "User does not exist.")
            return None

    def get_queryset(self):
        user = self.get_viewed_user()
        if not user:
            return Follow.objects.none()

        obj_type = self.request.GET.get('type')
        mutual_friends = Follow.objects.filter(follower=user).values_list('user', flat=True)

        if obj_type == 'following':
            mutual_follow = Follow.objects.filter(user=user).values_list('follower', flat=True)
            return Follow.objects.filter(follower=user).exclude(user__in=mutual_follow)
        elif obj_type == 'followers':
            return Follow.objects.filter(user=user).exclude(follower__in=mutual_friends)
        elif obj_type == 'friends':
            return Follow.objects.filter(user=user, follower__in=mutual_friends)
        elif obj_type == 'blocked':
            return Block.objects.filter(blocker=user)
        else:
            return Follow.objects.filter(follower=user)
