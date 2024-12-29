from django.shortcuts import redirect
from django.urls import reverse

from yumelinkapp.utils import oauth


def login(request):
    if not request.user.is_authenticated:
        return oauth.auth0.authorize_redirect(
            request, request.build_absolute_uri(reverse("callback")))
    return redirect(reverse('yumelinkapp:home'))
