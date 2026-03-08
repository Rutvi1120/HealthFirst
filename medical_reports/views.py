from django.shortcuts import render, redirect
from .models import MedicalReport
from django.contrib.auth.decorators import login_required


@login_required
def upload_report(request):

    if request.method == "POST":

        title = request.POST.get("title")
        file = request.FILES.get("report")

        MedicalReport.objects.create(
            user=request.user,
            title=title,
            report_file=file
        )

        return redirect("my_reports")

    return render(request, "medical_reports/upload_report.html")


@login_required
def my_reports(request):

    reports = MedicalReport.objects.filter(user=request.user)

    return render(request, "medical_reports/my_reports.html", {"reports": reports})