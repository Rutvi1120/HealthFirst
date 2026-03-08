from django.urls import path
from . import views

urlpatterns = [
    path("status/", views.ambulance_status, name="ambulance_status"),
]