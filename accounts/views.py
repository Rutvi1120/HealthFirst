from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # profile is auto-created by signal
            profile = user.profile
            profile.role = form.cleaned_data["role"]
            profile.mobile = form.cleaned_data["mobile"]
            profile.id_proof = form.cleaned_data.get("id_proof", "")
            profile.save()

            messages.success(request, "Registration successful. Please login.")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):
    role = request.user.profile.role

    if role == "CITIZEN":
        return render(request, "accounts/dashboards/citizen.html")
    elif role == "HOSPITAL":
        return render(request, "accounts/dashboards/hospital.html")
    elif role == "OFFICER":
        return render(request, "accounts/dashboards/officer.html")
    elif role == "SUPER":
        return render(request, "accounts/dashboards/super.html")

    return render(request, "accounts/dashboards/citizen.html")
