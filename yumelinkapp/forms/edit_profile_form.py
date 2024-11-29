from django import forms

from yumelinkapp.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'bio', 'profile', 'header', 'color']

