from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hospitals.models import Hospital
from .models import BloodAvailability
from .forms import BloodAvailabilityForm


@login_required
def manage_bloods(request):

    if not hasattr(request.user, 'profile') or request.user.profile.role != 'HOSPITAL':
        return redirect('landing')

    hospital, _ = Hospital.objects.get_or_create(admin=request.user)
    blood, _ = BloodAvailability.objects.get_or_create(hospital=hospital)

    if request.method == 'POST':
        form = BloodAvailabilityForm(request.POST, instance=blood)
        if form.is_valid():
            form.save()
            return redirect('bloodbank:manage_bloods')
    else:
        form = BloodAvailabilityForm(instance=blood)

    return render(request, 'hospitals/manage_bloods.html', {'form': form})


def view_bloods(request):
    blood_list = BloodAvailability.objects.select_related('hospital').all()
    return render(request, 'hospitals/view_bloods.html', {'blood_list': blood_list})