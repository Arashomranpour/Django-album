from django import forms
from .models import Photo

class photoform(forms.ModelForm):
    model=Photo
    fields="__all__"