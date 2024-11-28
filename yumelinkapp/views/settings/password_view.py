from django.views.generic import View
from django.shortcuts import render


class ChangePasswordView(View):
    template_name = 'registration/password.html'

    def get(self, request):
        context = {
            'title': 'Change Password',
        }
        return render(request, self.template_name, context)

    # def post(self, request):
