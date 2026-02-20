from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import Profile
from .models import Alert
from .forms import AlertForm

def is_officer(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile.role == "OFFICER"

@login_required
def add_alert(request):
    if not is_officer(request.user):
        return HttpResponseForbidden("Access Denied")

    if request.method == "POST":
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.created_by = request.user
            alert.save()
            return redirect("dashboard")
    else:
        form = AlertForm()

    return render(request, "alerts/add_alert.html", {"form": form})

@login_required
def edit_alert(request, alert_id):
    if not is_officer(request.user):
        return HttpResponseForbidden("Access Denied")

    alert = get_object_or_404(Alert, id=alert_id)

    if alert.created_by != request.user:
        return HttpResponseForbidden("You cannot edit this alert.")

    if request.method == "POST":
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = AlertForm(instance=alert)

    return render(request, "alerts/edit_alert.html", {"form": form, "alert": alert})

@login_required
def delete_alert(request, alert_id):
    if not is_officer(request.user):
        return HttpResponseForbidden("Access Denied")

    alert = get_object_or_404(Alert, id=alert_id)

    if alert.created_by != request.user:
        return HttpResponseForbidden("You cannot delete this alert.")

    if request.method == "POST":
        alert.delete()
        return redirect("dashboard")

    return render(request, "alerts/delete_alert.html", {"alert": alert})

@login_required
def citizen_alerts(request):
    alerts = Alert.objects.all().order_by("-created_at")
    return render(request, "alerts/citizen_alerts.html", {"alerts": alerts})