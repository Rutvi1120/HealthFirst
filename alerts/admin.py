from django.contrib import admin
from sos.models import SOSRequest


@admin.register(SOSRequest)
class SOSRequestAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "citizen",
        "accepted_by",
        "status",
        "latitude",
        "longitude",
        "created_at",
    )

    list_filter = ("status", "accepted_by")

    search_fields = ("citizen__username",)