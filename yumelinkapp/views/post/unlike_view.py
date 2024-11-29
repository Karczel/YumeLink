from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from yumelinkapp.models import User, Post, Like, Notification
from yumelinkapp.utils import LikeType


@login_required
def unlike(request, post_id):
    """Unlike a post."""
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        messages.warning(request, "This post does not exist.")
        return redirect("yumelinkapp:home")
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        messages.warning(request, "You have to log in as a user to unlike.")
        return redirect("yumelinkapp:post", pk=post_id)
    like = Like.objects.filter(user=user, post=post, type=LikeType.like.name).first()
    if like:
        like.delete()
    else:
        messages.warning(request, "You have never liked this post.")
    return redirect("yumelinkapp:post", pk=post_id)
