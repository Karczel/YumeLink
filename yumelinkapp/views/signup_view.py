from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from ..forms import SignupForm


class SignupView(View):
    """
    Register a new user.
    """

    def get(self, request):
        """Display the signup form."""
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        """Process the submitted signup form."""
        print(request.POST.get('csrfmiddlewaretoken', 'No CSRF Token Found'))

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passwd)

            login(request, user)
            return redirect('yumelinkapp:home')
        else:
            messages.error(request, "This form is invalid")
            return redirect(request, 'registration/signup.html', {'form': form})
