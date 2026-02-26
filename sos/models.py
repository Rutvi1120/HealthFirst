from django.db import models
from django.conf import settings
from hospitals.models import Hospital


class SOSRequest(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('RESOLVED', 'Resolved'),
    ]

    # Citizen who raised SOS
    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sos_requests'
    )

    # Location of emergency
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Optional emergency description
    description = models.TextField(blank=True, null=True)

    # SOS status
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    # Hospital that accepted SOS
    accepted_by = models.ForeignKey(
        Hospital,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='accepted_sos'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOS #{self.id} - {self.status}"