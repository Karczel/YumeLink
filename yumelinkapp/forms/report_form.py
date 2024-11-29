from django import forms

from yumelinkapp.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['type', 'content']
