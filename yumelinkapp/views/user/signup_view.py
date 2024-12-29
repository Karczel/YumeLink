from django.urls import reverse_lazy
from django.views.generic import View, FormView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from yumelinkapp.forms import SignupForm


class SignupView(FormView):
    """
    Register a new user.
    """
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('yumelinkapp:home')

    def get_initial(self):
        """Prefill the form with data from the session."""
        return self.request.session.pop('signup_data', {})

    def form_valid(self, form):
        """Handle valid form submissions."""
        # Save the user
        form.save()

        # Authenticate and log the user in
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)

        # Redirect to the success URL
        return super().form_valid(form)

    def form_invalid(self, form):
        """Handle invalid form submissions."""
        # Optionally add error messages
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))
