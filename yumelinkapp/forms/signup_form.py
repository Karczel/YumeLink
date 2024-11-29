from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from yumelinkapp.models import User


class SignupForm(UserCreationForm):
    """
    A form for registering a new user
    with their account details such as username, email, and password.
    """
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2'
        ]