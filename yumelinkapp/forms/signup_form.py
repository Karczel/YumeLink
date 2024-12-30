from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from yumelinkapp.models import User


class SignupForm(UserCreationForm):
    """
    A form for registering a new user
    with their account details such as username, email, and password.
    """
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'birthday',
            'password1', 'password2'
        ]
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name in initial and initial[field_name]:
                field.widget = forms.HiddenInput()  # Hide prefilled fields

