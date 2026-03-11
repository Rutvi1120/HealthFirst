from django.contrib import admin
from .models import Hospital, BedAvailability, Ambulance

admin.site.register(Hospital)
admin.site.register(BedAvailability)
admin.site.register(Ambulance)