app_name = "hospitals"

from django.urls import path,include
from . import views

urlpatterns = [
    path('manage-beds/', views.manage_beds, name='manage_beds'),
    path('view-beds/', views.view_beds, name='view_beds'),
    path('manage-bloods/', views.manage_bloods, name='manage_bloods'),
    path('view-bloods/', views.view_bloods, name='view_bloods'), 
]

