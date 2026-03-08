from django.db import models
from django.conf import settings


class MedicalReport(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="medical_reports"
    )

    title = models.CharField(max_length=100)

    report_file = models.FileField(
        upload_to="medical_reports/"
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title}"