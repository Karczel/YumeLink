from django import forms
from django.forms import modelformset_factory
from yumelinkapp.models import PostImage


class PostImageForm(forms.ModelForm):
    delete_image = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = PostImage
        fields = ['post', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['post'].initial = kwargs['instance'].post if kwargs['instance'] else None
        self.fields['post'].widget = forms.HiddenInput()


PostImageFormSet = modelformset_factory(
    PostImage,
    form=PostImageForm,
    extra=1,
    can_delete=True,
)
