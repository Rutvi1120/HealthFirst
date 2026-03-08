from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['hospital', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }