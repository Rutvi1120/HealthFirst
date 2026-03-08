from django.urls import path
from . import views

app_name = "bloodbank"

urlpatterns = [
    path('manage-bloods/', views.manage_bloods, name='manage_bloods'),
    path('view-bloods/', views.view_bloods, name='view_bloods'),
]