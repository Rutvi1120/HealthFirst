from django import forms
from .models import BedAvailability
from .models import BloodAvailability
from .models import Feedback

class BedAvailabilityForm(forms.ModelForm):
    class Meta:
        model = BedAvailability
        fields = ['icu_beds', 'oxygen_beds', 'general_beds']


class BloodAvailabilityForm(forms.ModelForm):
    class Meta:
        model = BloodAvailability
        exclude = ['hospital', 'last_updated']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['hospital', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }