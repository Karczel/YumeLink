from django import forms
from django.forms import modelformset_factory

from yumelinkapp.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False


TagFormSet = modelformset_factory(Tag, form=TagForm, extra=5, can_delete=True, max_num=5)
