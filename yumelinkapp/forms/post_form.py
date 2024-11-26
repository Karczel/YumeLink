from django import forms
from django.forms import modelformset_factory

from yumelinkapp.models import Post


class PostForm(forms.ModelForm):
    delete_image = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ['user', 'content', 'filter_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['user'].initial = instance.user
        self.fields['user'].widget = forms.HiddenInput()
