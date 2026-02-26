from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SOSRequest
from .forms import SOSForm
from hospitals.models import Hospital
import math


# ---------------------------
# Distance Calculator
# ---------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


# ---------------------------
# Citizen Raise SOS
# ---------------------------
@login_required
def raise_sos(request):

    if request.user.profile.role != "CITIZEN":
        messages.error(request, "Only citizens can raise SOS.")
        return redirect("landing")

    if request.method == "POST":
        form = SOSForm(request.POST)

        if form.is_valid():
            sos = form.save(commit=False)
            sos.citizen = request.user
            sos.status = "PENDING"
            sos.save()

            messages.success(request, f"SOS Created Successfully! ID: {sos.id}")
            return redirect("dashboard")

    else:
        form = SOSForm()

    return render(request, "sos/raise_sos.html", {"form": form})


# ---------------------------
# Hospital View Nearby SOS
# ---------------------------
@login_required
def hospital_sos_list(request):

    if request.user.profile.role != "HOSPITAL":
        messages.error(request, "Access denied.")
        return redirect("landing")

    hospital = get_object_or_404(Hospital, admin=request.user)

    pending_sos = SOSRequest.objects.filter(status="PENDING")
    nearby_sos = []

    for sos in pending_sos:
        if hospital.latitude and hospital.longitude:
            distance = calculate_distance(
                hospital.latitude,
                hospital.longitude,
                sos.latitude,
                sos.longitude
            )

            if distance <= 10:  # 10 km radius
                nearby_sos.append(sos)

    return render(request, "sos/hospital_sos_list.html", {"sos_list": nearby_sos})