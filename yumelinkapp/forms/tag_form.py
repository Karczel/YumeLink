from django import forms
from django.forms import modelformset_factory

from yumelinkapp.models import Tag


class TagForm(forms.ModelForm):
    delete_image = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Tag
        fields = ['content']


TagFormSet = modelformset_factory(Tag, form=TagForm, extra=1, can_delete=True, max_num=5)
