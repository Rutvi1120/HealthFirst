
from django.urls import path
from . import views

urlpatterns = [
    path('raise/', views.raise_sos, name='raise_sos'),
    path("hospital/", views.hospital_sos_list, name="hospital_sos_list"),
    path('decline/<int:sos_id>/', views.decline_sos, name='decline_sos'),
    path("accept_sos/<int:sos_id>/", views.accept_sos, name="accept_sos"),
    path('status/', views.citizen_sos_status, name='citizen_sos_status'),
    path("assign_ambulance/<int:sos_id>/", views.assign_ambulance, name="assign_ambulance"),
    path('status/', views.citizen_sos_status, name='citizen_sos_status'),
    path("update_status/<int:sos_id>/", views.update_status, name="update_status"),

]