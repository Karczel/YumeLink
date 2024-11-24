from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import Comment, User


@login_required
def delete_comment(request, post_id, pk):
    """Delete a comment to a post."""
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return redirect("yumelinkapp:home")
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return redirect("yumelinkapp:home")
    if user != comment.user:
        messages.warning(request, "You are not the owner of this comment.")
        return redirect("yumelinkapp:post", pk=post_id)
    comment.delete()
    return redirect("yumelinkapp:post", pk=post_id)

