from django.contrib import admin
from .models import Hospital, BedAvailability

admin.site.register(Hospital)
admin.site.register(BedAvailability)

