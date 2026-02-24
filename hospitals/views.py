from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hospital, BedAvailability
from .forms import BedAvailabilityForm


@login_required
def manage_beds(request):

    # Role check
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'HOSPITAL':
        return redirect('landing')   # change if needed

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
    beds = BedAvailability.objects.select_related('hospital').all()
    return render(request, 'hospitals/view_beds.html', {'beds': beds})
