from django import forms
from . import models


class calform(forms.ModelForm):
    class Meta:
        model=models.Cal
        fields='__all__'

class invform(forms.ModelForm):
    class Meta:
        model=models.Invoi
        fields='__all__'
