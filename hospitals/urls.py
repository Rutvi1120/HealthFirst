app_name = "hospitals"

from django.urls import path
from . import views

urlpatterns = [
    path('manage-beds/', views.manage_beds, name='manage_beds'),
    path('view-beds/', views.view_beds, name='view_beds'),
]