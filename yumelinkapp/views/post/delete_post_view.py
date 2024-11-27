from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Post


@login_required
def delete_post(request, pk):
    """Delete a post."""
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return redirect("yumelinkapp:home")
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return redirect("yumelinkapp:home")
    if user != post.user:
        messages.warning(request, "You are not the owner of this post.")
        return redirect("yumelinkapp:post", pk=pk)
    post.delete()
    return redirect("yumelinkapp:post", pk=pk)

