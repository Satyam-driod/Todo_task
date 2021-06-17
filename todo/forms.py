from django import forms
from django.forms import ModelForm


from .models import *
class WorkForm(ModelForm):
    title= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new work'}))

    class Meta:
        model=Work
        fields='__all__'
