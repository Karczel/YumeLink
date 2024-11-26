from django.views.generic import View
from django.shortcuts import render


class LoginView(View):
    template_name = 'yumelink/login.html'

    def get(self, request):
        """Handles GET requests to render the login page."""
        context = {
            'title': 'Login Page',
        }
        return render(request, self.template_name, context)
