from django import forms
from django.forms import modelformset_factory

from yumelinkapp.forms import BasePostImageFormSet
from yumelinkapp.models import PostImage


class PostTagForm(forms.ModelForm):
    delete_image = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = PostImage
        fields = ['image', 'post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['post'].initial = instance
        self.fields['post'].widget = forms.HiddenInput()
#
# PostImageFormSet = modelformset_factory(
#     PostImage,
#     form=PostTagForm,
#     formset=BasePostImageFormSet,
#     extra=1,
#     can_delete=True,
# )
