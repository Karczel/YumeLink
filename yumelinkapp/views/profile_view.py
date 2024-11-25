from django.views.generic import ListView
from yumelinkapp.models import User


class ProfileView(ListView):
    model = User
    template_name = 'yumelink/user_profile.html'
    context_object_name = 'user_profile'

    def get_queryset(self):
        return User.objects.all().order_by('name')

