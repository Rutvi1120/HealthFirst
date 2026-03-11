from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sos.models import SOSRequest
from hospitals.models import Ambulance
from hospitals.models import Hospital

def ambulance_status(request):

    hospital = Hospital.objects.filter(admin=request.user).first()

    ambulances = Ambulance.objects.filter(hospital=hospital)

    return render(request, "ambulances/ambulance_status.html", {
        "ambulances": ambulances
    })

    