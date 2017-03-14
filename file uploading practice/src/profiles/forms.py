from django import forms
from .models import myprofile

class registrationform(forms.ModelForm):
    class Meta:
        model = myprofile
        fields="__all__"