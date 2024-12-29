from urllib.parse import urlencode, quote_plus

from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse


def logout(request):
    request.session.clear()
    logout_url = f"https://{settings.AUTH0_DOMAIN}/v2/logout?" \
                 + urlencode(
        {
            "returnTo": request.build_absolute_uri(reverse("yumelink:home")),
            "client_id": settings.AUTH0_CLIENT_ID,
        }, quote_via=quote_plus,
    )
    return redirect(logout_url)
