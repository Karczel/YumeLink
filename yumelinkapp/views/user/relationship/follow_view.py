from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User, Follow


@login_required
def follow(request, username):
    user = User.objects.get(id=request.user.id)
    followed_user = User.objects.filter(username=username).first()
    follow_obj = Follow.objects.filter(follower=user, user=followed_user).first()
    if follow_obj:
        messages.error(request, "You have already followed this user.")
    else:
        Follow.objects.create(follower=user, user=followed_user)
    return redirect('yumelinkapp:user_profile', username)
