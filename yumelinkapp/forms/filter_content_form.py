from django import forms

from yumelinkapp.models import User


class FilterContentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['filter_content']