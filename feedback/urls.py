from django.urls import path
from . import views

app_name = "feedback"

urlpatterns = [
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('view-feedback/', views.view_feedback, name='view_feedback'),
]