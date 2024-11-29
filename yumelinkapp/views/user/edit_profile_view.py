from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView

from yumelinkapp.forms import EditProfileForm
from yumelinkapp.models import User


class EditProfileView(LoginRequiredMixin, UpdateView):
    """
    View for updating User details.
    """
    model = User
    form_class = EditProfileForm
    template_name = 'user/edit_user_profile.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context

    def get(self, request, *args, **kwargs):
        super(EditProfileView, self).get(request, *args, **kwargs)
        self.object = self.get_object()
        current_user = User.objects.get(id=request.user.id)
        if self.object != current_user:
            messages.warning(request, 'You can only edit your own profile.')
            return redirect('yumelinkapp:home')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        current_user = User.objects.get(id=request.user.id)
        if self.object != current_user:
            messages.warning(request, 'You can only edit your own profile.')
            return redirect('yumelinkapp:home')
        form = self.form_class(request.POST, request.FILES, instance=self.object)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('yumelinkapp:user_profile', username=self.object.username)
        else:
            # Debug uploaded files and errors
            messages.error(request, f"Form errors: {form.errors}")
            if not request.FILES:
                messages.error(request, "No files were uploaded.")
        # messages.info(request,request.POST)
        # messages.info(request,request.FILES)

        return self.render_to_response(self.get_context_data(form=form))