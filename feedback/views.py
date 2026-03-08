from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hospitals.models import Hospital
from .models import Feedback
from .forms import FeedbackForm


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