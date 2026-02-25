from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hospital, BedAvailability,BloodAvailability,Feedback
from .forms import BedAvailabilityForm,BloodAvailabilityForm,FeedbackForm


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
            return redirect('hospitals:manage_bloods')
    else:
        form = BloodAvailabilityForm(instance=blood)

    return render(request, 'hospitals/manage_bloods.html', {'form': form})


def view_bloods(request):
    blood_list = BloodAvailability.objects.select_related('hospital').all()
    return render(request, 'hospitals/view_bloods.html', {'blood_list': blood_list})


@login_required
def submit_feedback(request):

    if not hasattr(request.user, 'profile') or request.user.profile.role != 'CITIZEN':
        return redirect('landing')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.citizen = request.user
            feedback.save()
            return redirect('landing')
    else:
        form = FeedbackForm()

    return render(request, 'hospitals/submit_feedback.html', {'form': form})

@login_required
def view_feedback(request):

    if not hasattr(request.user, 'profile') or request.user.profile.role != 'HOSPITAL':
        return redirect('landing')

    hospital = Hospital.objects.get(admin=request.user)
    feedbacks = Feedback.objects.filter(hospital=hospital).select_related('citizen')

    return render(request, 'hospitals/view_feedback.html', {'feedbacks': feedbacks})