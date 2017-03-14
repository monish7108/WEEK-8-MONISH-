from django import forms

from .models import cust_details, personal_details

class registration(forms.ModelForm):

    class Meta:
        model = cust_details
        fields="__all__"

class personal(forms.ModelForm):

    class Meta:
        model = personal_details
        fields="__all__"