from django import forms
from django.contrib.auth.models import User
from .models import Profile
from hospitals.models import Hospital


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    role = forms.ChoiceField(
        choices=[choice for choice in Profile.ROLE_CHOICES if choice[0] != "SUPER"]
    )

    mobile = forms.CharField(max_length=15)
    id_proof = forms.CharField(max_length=50, required=False)

    # hospital dropdown (only for hospital admin)
    hospital = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),
        required=False,
        empty_label="Select Hospital"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")

        if mobile and Profile.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("This mobile number is already registered.")

        return mobile

    def clean(self):
        cleaned = super().clean()

        p1 = cleaned.get("password")
        p2 = cleaned.get("confirm_password")
        role = cleaned.get("role")
        hospital = cleaned.get("hospital")

        # password match check
        if p1 and p2 and p1 != p2:
            self.add_error("confirm_password", "Passwords do not match.")

        # hospital required only for hospital admin
        if role == "HOSPITAL" and not hospital:
            self.add_error("hospital", "Please select a hospital.")

        return cleaned