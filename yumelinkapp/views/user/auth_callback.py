from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from yumelinkapp.forms import SignupForm
from yumelinkapp.models import User
from yumelinkapp.utils import oauth
from django.contrib.auth import login as django_login





def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    if not token:
        messages.error(request, "Authentication failed. Please try again.")
        return redirect(reverse('signup'))

    user_info = token['userinfo']
    messages.info(user_info)
    try:
        user = User.objects.get(username=user_info['sub'])
        django_login(request, user)
    except User.DoesNotExist:
        request.session['signup_data'] = {
            'email': user_info['email'],
            'first_name': user_info.get('given_name', ''),
            'last_name': user_info.get('family_name', ''),
            'birthday': user_info.get(f'https://{request.get_host()}/birthday', ''),
        }
        return redirect(reverse('signup'))
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("yumelinkapp:home")))
