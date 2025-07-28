from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['ho_ten', 'ngay_sinh']
        widgets = {
            'ngay_sinh': forms.DateInput(attrs={'type': 'date'})
        }