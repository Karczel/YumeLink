# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
#
#
# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'user/user_profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Pass the currently logged-in user's information to the template
#         context['user_profile'] = self.request.user
#         return context

from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = 'user/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Pass the logged-in user's information if they are authenticated
            context['user_profile'] = self.request.user
        else:
            # Provide default values for unauthenticated users
            context['user_profile'] = {
                'name': 'Guest User',
                'email': 'N/A',
                'username': 'Guest',
                'bio': 'You are currently viewing the site as a guest.',
            }
        return context
