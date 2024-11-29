from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Post, Like
from yumelinkapp.utils import LikeType


@login_required
def love(request, post_id):
    """Love a post."""
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        messages.warning(request, "This post does not exist.")
        return redirect("yumelinkapp:home")
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        messages.warning(request, "You have to log in as a user to love.")
        return redirect("yumelinkapp:post", pk=post_id)
    Like.objects.create(user=user, post=post, type=LikeType.love.name)
    return redirect("yumelinkapp:post", pk=post_id)
