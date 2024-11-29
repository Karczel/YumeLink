from django import forms

class InviteChatForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
