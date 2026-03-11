from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hospital, BedAvailability
from .forms import BedAvailabilityForm
from .models import Ambulance
from .forms import AmbulanceForm
from django.shortcuts import render, redirect
from accounts.models import Profile


@login_required
def hospital_dashboard(request):
    return render(request, "accounts/dashboards/hospital.html")

@login_required
def manage_beds(request):

    if not hasattr(request.user, 'profile') or request.user.profile.role != 'HOSPITAL':
        return redirect('landing')

    hospital, _ = Hospital.objects.get_or_create(admin=request.user)
    bed, _ = BedAvailability.objects.get_or_create(hospital=hospital)

    if request.method == 'POST':
        form = BedAvailabilityForm(request.POST, instance=bed)
        if form.is_valid():
            form.save()
            return redirect('hospitals:manage_beds')
    else:
        form = BedAvailabilityForm(instance=bed)

    return render(request, 'hospitals/manage_beds.html', {'form': form})


def view_beds(request):

    hospital_id = request.GET.get("hospital")

    beds = BedAvailability.objects.all()

    if hospital_id:
        beds = beds.filter(hospital_id=hospital_id)

    hospitals = Hospital.objects.all()

    return render(request, "hospitals/view_beds.html", {
        "beds": beds,
        "hospitals": hospitals
    })

def view_bloods(request):
    return render(request, "hospitals/view_bloods.html")


def manage_bloods(request):
    return render(request, "hospitals/manage_bloods.html")


def submit_feedback(request):
    return render(request, "hospitals/submit_feedback.html")


def view_feedback(request):
    return render(request, "hospitals/view_feedback.html")

# code for hash generation
import hashlib

def generate_hash(file):
    hasher = hashlib.sha256()

    for chunk in file.chunks():
        hasher.update(chunk)

    return hasher.hexdigest()

from .models import MedicalReport

def upload_report(request):

    if request.method == "POST":

        patient_name = request.POST.get("patient_name")
        report_type = request.POST.get("report_type")
        report_date = request.POST.get("report_date")

        file = request.FILES["report_file"]

        hash_value = generate_hash(file)

        MedicalReport.objects.create(
            patient_name=patient_name,
            report_type=report_type,
            report_date=report_date,
            report_file=file,
            report_hash=hash_value
        )

        return render(request,"hospitals/upload_success.html")

    return render(request,"hospitals/upload_report.html")

def verify_report(request):

    result = None

    if request.method == "POST":

        patient_name = request.POST.get("patient_name")
        report_type = request.POST.get("report_type")
        report_date = request.POST.get("report_date")
        file = request.FILES["report_file"]

        uploaded_hash = generate_hash(file)

        reports = MedicalReport.objects.filter(
            patient_name=patient_name,
            report_type=report_type,
            report_date=report_date
        )

        if reports.exists():

            report = reports.first()

            if report.report_hash == uploaded_hash:
                result = "Report is Authentic ✅"
            else:
                result = "Report Modified ❌"

        else:
            result = "Report not found in database"

    return render(request,"hospitals/verify_report.html",{"result":result})

from .models import Ambulance, Hospital
from .forms import AmbulanceForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def register_ambulance(request):

    hospital = Hospital.objects.filter(admin=request.user).first()

    if request.method == "POST":

        form = AmbulanceForm(request.POST)

        if form.is_valid():
            ambulance = form.save(commit=False)
            ambulance.hospital = hospital
            ambulance.save()

            return redirect("ambulance_status")

    else:
        form = AmbulanceForm()

    return render(request, "hospitals/register_ambulance.html", {"form": form})

