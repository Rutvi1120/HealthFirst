from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SOSRequest
from .forms import SOSForm
from hospitals.models import Hospital, Ambulance
import math

# Distance calculation (for future use)
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
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

# Citizen raises SOS
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

# Hospital sees SOS list
@login_required
def hospital_sos_list(request):
    if request.user.profile.role != "HOSPITAL":
        messages.error(request, "Access denied.")
        return redirect("landing")

    hospital = get_object_or_404(Hospital, admin=request.user)
    pending_sos = SOSRequest.objects.filter(status="PENDING")
    accepted_sos = SOSRequest.objects.filter(accepted_by=hospital)
    sos_list = list(pending_sos) + list(accepted_sos)
    ambulances = Ambulance.objects.filter(status="AVAILABLE", hospital=hospital)

    return render(request, "sos/hospital_sos_list.html", {"sos_list": sos_list, "ambulances": ambulances})

# Accept SOS
@login_required
def accept_sos(request, sos_id):
    hospital = get_object_or_404(Hospital, admin=request.user)
    sos = get_object_or_404(SOSRequest, id=sos_id)
    if sos.status == "PENDING":
        sos.status = "ACCEPTED"
        sos.accepted_by = hospital
        sos.save()
    return redirect("hospital_sos_list")

# Decline SOS
@login_required
def decline_sos(request, sos_id):
    sos = get_object_or_404(SOSRequest, id=sos_id)
    sos.status = "DECLINED"
    sos.save()
    messages.success(request, "SOS request declined successfully!")
    return redirect("hospital_sos_list")

# Assign Ambulance
@login_required
def assign_ambulance(request, sos_id):
    sos = get_object_or_404(SOSRequest, id=sos_id)
    if request.method == "POST":
        ambulance_id = request.POST.get("ambulance")
        ambulance = get_object_or_404(Ambulance, id=ambulance_id, status="AVAILABLE")
        ambulance.status = "BUSY"
        ambulance.current_status = f"SOS #{sos.id}"
        ambulance.save()
        sos.ambulance = ambulance
        sos.status = "DISPATCHED"
        sos.save()
    return redirect("hospital_sos_list")

# Update SOS status (ON_ROUTE, ARRIVED, COMPLETED)
@login_required
def update_status(request, sos_id):
    sos = get_object_or_404(SOSRequest, id=sos_id)
    allowed_statuses = ["ON_ROUTE", "ARRIVED", "COMPLETED"]
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status not in allowed_statuses:
            messages.error(request, "Invalid status!")
        else:
            sos.status = new_status
            if new_status == "COMPLETED" and sos.ambulance:
                amb = sos.ambulance
                amb.status = "AVAILABLE"
                amb.current_status = ""
                amb.save()
            sos.save()
            messages.success(request, f"SOS status updated to {new_status}")
    return redirect("hospital_sos_list")

# Citizen checks their SOS status
@login_required
def citizen_sos_status(request):
    if request.user.profile.role != "CITIZEN":
        return redirect("landing")
    sos_list = SOSRequest.objects.filter(citizen=request.user).order_by('-created_at')
    return render(request, "sos/citizen_sos_status.html", {"sos_list": sos_list})
