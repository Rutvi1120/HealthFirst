from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sos.models import SOSRequest

@login_required
def ambulance_status(request):

    sos_requests = SOSRequest.objects.filter(citizen=request.user).order_by("-created_at")

    return render(
        request,
        "ambulances/ambulance_status.html",
        {"sos_requests": sos_requests}
    )