from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import User


@login_required
def delete_user(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect('yumelinkapp:home')
