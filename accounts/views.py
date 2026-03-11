from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from django.contrib.auth.models import User

from .forms import RegisterForm
from .models import Profile

from alerts.models import Alert
from hospitals.models import Hospital


def _canonical_role(raw_role):
    value = (raw_role or "").strip().upper().replace("-", " ").replace("_", " ")

    if "HOSP" in value:
        return "HOSPITAL"
    if "OFFIC" in value:
        return "OFFICER"
    if "SUPER" in value:
        return "SUPER"

    return "CITIZEN"


@never_cache
def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            # username exists check
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return render(request, "accounts/register.html", {"form": form})

            # email exists check
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return render(request, "accounts/register.html", {"form": form})

            # create user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # profile created by signal
            profile = user.profile
            profile.role = form.cleaned_data["role"]
            profile.mobile = form.cleaned_data["mobile"]
            profile.id_proof = form.cleaned_data.get("id_proof", "")
            profile.save()

            # assign hospital if hospital admin
            hospital = form.cleaned_data.get("hospital")

            if profile.role == "HOSPITAL" and hospital:
                hospital.admin = user
                hospital.save()

            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


@never_cache
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            profile, _ = Profile.objects.get_or_create(user=user)

            canonical = _canonical_role(profile.role)

            if profile.role != canonical:
                profile.role = canonical
                profile.save(update_fields=["role"])

            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):

    profile, _ = Profile.objects.get_or_create(user=request.user)
    role = _canonical_role(profile.role)

    if role == "CITIZEN":

        alerts = Alert.objects.filter(is_active=True).order_by("-created_at")[:5]

        return render(
            request,
            "accounts/dashboards/citizen.html",
            {"alerts": alerts}
        )

    elif role == "HOSPITAL":

        hospital = Hospital.objects.filter(admin=request.user).first()

        return render(
            request,
            "accounts/dashboards/hospital.html",
            {"hospital": hospital}
        )

    elif role == "SUPER":

        return render(request, "accounts/dashboards/super.html")

    elif role == "OFFICER":

        alerts = Alert.objects.filter(created_by=request.user).order_by("-created_at")

        return render(
            request,
            "accounts/dashboards/officer.html",
            {"alerts": alerts}
        )

    alerts = Alert.objects.filter(is_active=True).order_by("-created_at")[:5]

    return render(
        request,
        "accounts/dashboards/citizen.html",
        {"alerts": alerts}
    )