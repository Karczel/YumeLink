from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Block


@login_required
def unblock(request, username):
    user = User.objects.get(id=request.user.id)
    blocked_user = User.objects.filter(username=username).first()
    block_obj = Block.objects.filter(blocker=user, blocked=blocked_user).first()
    if block_obj:
        block_obj.delete()
    else:
        messages.error(request, "You have never blocked this user.")
    return redirect('yumelinkapp:user_profile', username)
