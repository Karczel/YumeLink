from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from yumelinkapp.models import User, Post, Like, Notification, Share
from yumelinkapp.utils import LikeType, ShareType


@login_required
def unreblog(request, post_id):
    """Unreblog a post."""
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        messages.warning(request, "This post does not exist.")
        return redirect("yumelinkapp:home")
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        messages.warning(request, "You have to log in as a user to unreblog.")
        return redirect("yumelinkapp:post", pk=post_id)
    share = Share.objects.filter(user=user, post=post, type=ShareType.reblog.name).first()
    if share:
        share.delete()
        messages.success(request, f'Post unreblogged successfully!')
    else:
        messages.warning(request, "You have never reblogged this post.")
    return redirect("yumelinkapp:post", pk=post_id)
