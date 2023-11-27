"""Urls for adding clients to the page"""
from django.urls import path
from . import views


urlpatterns = [
  path('client_form/', views.client_form, name='client_form'),
  path('add_client/', views.add_client, name='add_client'),
  path('edit_client/<int:pk>/', views.edit_client, name='edit_client'),
  path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
]