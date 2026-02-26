from django.urls import path
from . import views

urlpatterns = [
    path('raise/', views.raise_sos, name='raise_sos'),
    path('hospital/', views.hospital_sos_list, name='hospital_sos_list'),
]