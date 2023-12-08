"""client_management URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include("allauth.urls")),
    path('home/', include('home.urls')),
    path('owners/', include('owners.urls')),
    path('clients/', include('clients.urls', namespace='clients')),
]
