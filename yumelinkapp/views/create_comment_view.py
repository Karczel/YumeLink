from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Comment, Post


@login_required
def create_comment(request, post_id):
    """Create a comment to a post."""
    if request.method == 'POST':
        content = request.POST.get('content')
        if not content:
            messages.warning(request, "Content is required.")
            return redirect("yumelinkapp:post", pk=post_id)
        try:
            user = User.objects.get(id=request.user.id)
            post = Post.objects.get(id=post_id)
        except User.DoesNotExist or Post.DoesNotExist:
            return redirect("yumelinkapp:post", pk=post_id)
        Comment.objects.create(user=user, post=post, content=content)
        return redirect("yumelinkapp:post", pk=post_id)
    return redirect("yumelinkapp:post", pk=post_id)

