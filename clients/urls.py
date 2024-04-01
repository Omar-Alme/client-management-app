"""Urls for adding clients to the page"""
from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('client_form/', views.client_form, name='client_form'),
  path('edit_client/<int:pk>/', views.edit_client, name='edit_client'),
  path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
]
