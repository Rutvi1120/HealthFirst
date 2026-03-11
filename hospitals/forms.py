from django import forms
from .models import BedAvailability
from .models import Ambulance

class BedAvailabilityForm(forms.ModelForm):
    class Meta:
        model = BedAvailability
        fields = ['icu_beds', 'oxygen_beds', 'general_beds']

class AmbulanceForm(forms.ModelForm):

    class Meta:
        model = Ambulance
        fields = [
            "vehicle_number",
            "driver_name",
            "driver_mobile"
        ]