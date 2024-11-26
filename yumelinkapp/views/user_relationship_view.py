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
        return context

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
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
