from django.db import models
from django.conf import settings
from hospitals.models import Hospital


class Feedback(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='feedbacks')
    citizen = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.citizen.username} to {self.hospital.name}"