from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("ambulance/", include("ambulances.urls")), 
    path('alerts/', include('alerts.urls')),
    path('hospitals/', include('hospitals.urls')),
    path('sos/', include('sos.urls')),
    path('reports/', include('medical_reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
