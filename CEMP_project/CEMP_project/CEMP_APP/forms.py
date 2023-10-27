from django import forms
from django.core import validators
from .models import detailsclass

class detailsform(forms.ModelForm):
    class Meta:
        model=detailsclass
        fields=['s_name','dob','age','phno','email','address']