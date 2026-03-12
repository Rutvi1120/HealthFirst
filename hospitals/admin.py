
from django.contrib import admin
from .models import Hospital, BedAvailability, Ambulance

# Hospital and BedAvailability admin
admin.site.register(Hospital)
admin.site.register(BedAvailability)

# Ambulance admin
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ("vehicle_number", "driver_name", "hospital", "status")
    readonly_fields = ("hospital",)  # hospital is read-only in admin form

    def save_model(self, request, obj, form, change):
        # Automatically assign the hospital if creating new ambulance
        if not change:  # new object
            hospital = Hospital.objects.filter(admin=request.user).first()
            if hospital:
                obj.hospital = hospital
        super().save_model(request, obj, form, change)

admin.site.register(Ambulance, AmbulanceAdmin)