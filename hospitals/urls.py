from django.urls import path
from . import views

app_name = "hospitals"

urlpatterns = [
    path("dashboard/", views.hospital_dashboard, name="hospital_dashboard"),
    path('upload-report/', views.upload_report, name='upload_report'),
    path('verify-report/', views.verify_report, name='verify_report'),

    path('view-beds/', views.view_beds, name='view_beds'),
    path('manage-beds/', views.manage_beds, name='manage_beds'),

    path('view-bloods/', views.view_bloods, name='view_bloods'),
    path('manage-bloods/', views.manage_bloods, name='manage_bloods'),

    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('view-feedback/', views.view_feedback, name='view_feedback'),
    path("register-ambulance/", views.register_ambulance, name="register_ambulance"),
]