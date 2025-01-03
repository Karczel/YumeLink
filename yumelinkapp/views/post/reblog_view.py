from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Post, Share
from yumelinkapp.utils import ShareType


@login_required
def reblog(request, post_id):
    """Reblog a post."""
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        messages.warning(request, "This post does not exist.")
        return redirect("yumelinkapp:home")
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        messages.warning(request, "You have to log in as a user to reblog.")
        return redirect("yumelinkapp:post", pk=post_id)
    Share.objects.create(
        user=user,
        post=post,
        share_type=ShareType.reblog.name)
    messages.success(request, f'Post reblogged successfully!')

    return redirect("yumelinkapp:post", pk=post_id)
