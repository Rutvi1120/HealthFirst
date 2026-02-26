from django import forms
from .models import SOSRequest


class SOSForm(forms.ModelForm):
    class Meta:
        model = SOSRequest
        fields = ['latitude', 'longitude', 'description']

        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }