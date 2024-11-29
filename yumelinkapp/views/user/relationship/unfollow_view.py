from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from yumelinkapp.models import User, Follow, Notification


@login_required
def unfollow(request, username):
    user = User.objects.get(id=request.user.id)
    followed_user = User.objects.filter(username=username).first()
    follow_obj = Follow.objects.filter(follower=user, user=followed_user).first()
    if follow_obj:
        follow_obj.delete()
    else:
        messages.error(request, "You have never followed this user.")
    return redirect('yumelinkapp:user_profile', username)
