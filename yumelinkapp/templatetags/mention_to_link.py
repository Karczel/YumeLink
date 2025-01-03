import re
from django import template
from django.urls import reverse
from yumelinkapp.models import User

register = template.Library()


@register.filter(name='mention_to_link')
def mention_to_link(value):
    """
    Convert @username mentions in the text to a link to the user's profile.
    """

    def replace_mention(match):
        username = match.group(1)
        try:
            user = User.objects.get(username=username)
            profile_url = reverse('yumelinkapp:user_profile', kwargs={'username': user.username})
            return f'<a href="{profile_url}">@{username}</a>'
        except User.DoesNotExist:
            return match.group(0)
    return re.sub(r'@(\w+)', replace_mention, value)
