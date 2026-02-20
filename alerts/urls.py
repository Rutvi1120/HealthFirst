from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_alert, name="add_alert"),
    path("edit/<int:alert_id>/", views.edit_alert, name="edit_alert"),
    path("delete/<int:alert_id>/", views.delete_alert, name="delete_alert"),
    path("citizen/", views.citizen_alerts, name="citizen_alerts"),
]