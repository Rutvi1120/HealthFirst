from django import forms
from .models import BedAvailability


class BedAvailabilityForm(forms.ModelForm):
    class Meta:
        model = BedAvailability
        fields = ['icu_beds', 'oxygen_beds', 'general_beds']