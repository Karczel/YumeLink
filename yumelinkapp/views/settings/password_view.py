from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password.html'
    success_url = reverse_lazy('yumelinkapp:settings')  # Redirect after successful password change
