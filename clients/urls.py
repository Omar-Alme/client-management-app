"""Urls for adding clients to the page"""
from django.urls import path
from . import views

urlpatterns = [
  path  ('', views.dashboard, name='dashboard'),
]
