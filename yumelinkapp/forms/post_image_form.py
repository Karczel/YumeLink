from django import forms
from django.forms import modelformset_factory
from yumelinkapp.models import PostImage


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']


PostImageFormSet = modelformset_factory(
    PostImage,
    form=PostImageForm,
    extra=1,
    can_delete=True,
)
