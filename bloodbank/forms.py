from django import forms
from .models import BloodAvailability


class BloodAvailabilityForm(forms.ModelForm):
    class Meta:
        model = BloodAvailability
        exclude = ['hospital', 'last_updated']