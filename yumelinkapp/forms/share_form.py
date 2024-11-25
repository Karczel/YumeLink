from django import forms
from yumelinkapp.utils import ShareType


class ShareForm(forms.Form):
    """
    Form for sharing a post (via a link or reblog).
    """
    share_type = forms.ChoiceField(choices=ShareType.choices(), label="Share Type", widget=forms.Select())