from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from yumelinkapp.models import User, Post, Like, Notification
from yumelinkapp.utils import LikeType


@login_required
def unlove(request, post_id):
    """Unlove a post."""
    try:
        user = User.objects.get(id=request.user.id)
        post = Post.objects.get(id=post_id)
    except User.DoesNotExist:
        messages.warning(request, "You have to log in as a user to like.")
        return redirect("yumelinkapp:post", pk=post_id)
    love = Like.objects.filter(user=user, post=post, type=LikeType.love.name).first()
    if love:
        love.delete()
    else:
        messages.warning(request, "You have never loved this post.")
    return redirect("yumelinkapp:post", pk=post_id)