# sos/models.py
from django.db import models
from django.conf import settings
from hospitals.models import Hospital, Ambulance  # Make sure Ambulance model exists

class SOSRequest(models.Model):
    STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("ACCEPTED", "Accepted"),
    ("DISPATCHED", "Ambulance Dispatched"),
    ("ON_ROUTE", "On Route"),
    ("ARRIVED", "Ambulance Arrived"),
    ("COMPLETED", "Completed"),
    ("DECLINED", "Declined"),
]
    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="PENDING"
)

    # Citizen who raised SOS
    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sos_requests"
    )

    # Hospital that accepted the SOS
    accepted_by = models.ForeignKey(
        Hospital,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="accepted_sos"
    )

    # Assigned ambulance (optional)
    ambulance = models.ForeignKey(
        Ambulance,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_sos"
    )

    # Emergency location
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Optional description
    description = models.TextField(blank=True, null=True)

    # SOS status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOS #{self.id} - {self.status}"