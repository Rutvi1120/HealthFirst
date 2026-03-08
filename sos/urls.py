from django.urls import path
from . import views

urlpatterns = [
    path('raise/', views.raise_sos, name='raise_sos'),

    # Hospital dashboard to see SOS
    path('hospital/', views.hospital_sos_list, name='hospital_sos_list'),

    # Hospital accepts SOS
    path('accept/<int:sos_id>/', views.accept_sos, name='accept_sos'),

    # Hospital updates ambulance status
    path('update-status/<int:sos_id>/', views.update_status, name='update_status'),
]