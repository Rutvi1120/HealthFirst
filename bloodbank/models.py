from django.db import models
from hospitals.models import Hospital


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