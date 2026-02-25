from django.db import models
from django.conf import settings

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BedAvailability(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    icu_beds = models.IntegerField(default=0)
    oxygen_beds = models.IntegerField(default=0)
    general_beds = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hospital.name} Bed Status"

class BloodAvailability(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)

    a_positive = models.IntegerField(default=0)
    a_negative = models.IntegerField(default=0)
    b_positive = models.IntegerField(default=0)
    b_negative = models.IntegerField(default=0)
    o_positive = models.IntegerField(default=0)
    o_negative = models.IntegerField(default=0)
    ab_positive = models.IntegerField(default=0)
    ab_negative = models.IntegerField(default=0)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hospital.name} Blood Stock"

class Feedback(models.Model):
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='feedbacks')
    citizen = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.citizen.username} to {self.hospital.name}"