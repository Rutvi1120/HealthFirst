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
