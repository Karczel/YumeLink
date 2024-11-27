from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Block, Follow


@login_required
def block(request, username):
    user = User.objects.get(id=request.user.id)
    blocked_user = User.objects.filter(username=username).first()
    block_obj = Block.objects.filter(blocker=user, blocked=blocked_user).first()
    if block_obj:
        messages.error(request, "You have already blocked this user.")
    else:
        Follow.objects.filter(user=user, follower=blocked_user).delete()
        Block.objects.create(blocker=user, blocked=blocked_user)
    return redirect('yumelinkapp:user_profile', username)
