from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from yumelinkapp.models import User, Post, Like, Share, PostImage
from yumelinkapp.utils import ShareType, LikeType


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        """Retrieve the user by username."""
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the currently logged-in user's information to the template
        user = self.get_object()

        context['likes'] = Like.objects.filter(
            post_id__in=Post.objects.filter(user=user).values_list('id', flat=True)).count()

        obj_type = self.request.GET.get('type')

        if obj_type == 'like':
            liked_post_ids = Like.objects.filter(user=user, type=LikeType.like.name).values_list('post_id', flat=True)
            posts = Post.objects.filter(id__in=liked_post_ids)
        elif obj_type == 'love':
            loved_post_ids = Like.objects.filter(user=user, type=LikeType.love.name).values_list('post_id', flat=True)
            posts = Post.objects.filter(id__in=loved_post_ids)
        elif obj_type == 'repost':
            shared_post_ids = Share.objects.filter(user=user, type=ShareType.reblog.name).values_list('post_id', flat=True)
            posts = Post.objects.filter(id__in=shared_post_ids)
        else:
            posts = Post.objects.filter(user=user)

        context['posts_with_images'] = [
            {
                'post': post,
                'post_images': PostImage.objects.filter(post=post)
            }
            for post in posts.order_by('-timestamp')  # Order posts by timestamp
        ]

        context['current_user'] = User.objects.get(id=self.request.user.id)
        return context
