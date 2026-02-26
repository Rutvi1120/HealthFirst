from django.contrib import admin
from .models import Hospital, BedAvailability, BloodAvailability, Feedback

admin.site.register(Hospital)
admin.site.register(BedAvailability)
admin.site.register(BloodAvailability)
admin.site.register(Feedback)