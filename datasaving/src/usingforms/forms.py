from django import forms
from .models import customer_details, personaldetails

class register2(forms.ModelForm):
    # cust_name = forms.CharField(max_length=20)
    # cust_id = forms.IntegerField()
    class Meta:
        model= customer_details
        fields="__all__"

class personal2(forms.ModelForm):

    class Meta:
        model = personaldetails
        fields="__all__"