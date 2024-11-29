from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from yumelinkapp.models import User, Post, Like, Share, PostImage, Follow, Block
from yumelinkapp.utils import ShareType, LikeType


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_profile.html'

    def get_object(self):
        """Retrieve the user by username."""
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the currently logged-in user's information to the template
        user = self.get_object()

        context['following'] = Follow.objects.filter(follower=user).count()
        context['followers'] = Follow.objects.filter(user=user).count()
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
            shared_post_ids = Share.objects.filter(user=user, share_type=ShareType.reblog.name).values_list('post_id', flat=True)
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

        user = User.objects.get(id=self.request.user.id)
        viewed_user = self.get_object()

        context['current_user'] = user
        context['viewed_user'] = viewed_user
        context['same_user'] = user == viewed_user

        if user != viewed_user:
            context['follow'] = Follow.objects.filter(follower=user, user=viewed_user).exists()
            context['is_block'] = Block.objects.filter(blocker=user, blocked=viewed_user).exists()

        # messages.info(self.request, context)
        return context

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        current_user = User.objects.get(id=request.user.id)

        # Check if the current user is blocked by the post owner
        is_blocked = Block.objects.filter(blocker=user, blocked=current_user).exists()

        if is_blocked:
            messages.warning(request, "You are blocked by this user")
            # Redirect to a "blocked" page or another relevant page
            return redirect('yumelinkapp:home')

        return super().get(request, *args, **kwargs)
